from rest_framework import viewsets
from .models import Student, Professor
from .serializers import StudentSerializer, ProfessorSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Professor
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from datetime import timedelta

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class RegisterStudentView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        name = request.data.get('name')
        department = request.data.get('department')
        student_id = request.data.get('student_id')
        year = request.data.get('year')

        user = User.objects.create_user(username=username, password=password, email=email)
        student = Student.objects.create(name=name, department=department, student_id=student_id, year=year, user=user)

        return Response({"message": "학생 계정 생성 성공"})


class RegisterProfessorView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        name = request.data.get('name')
        department = request.data.get('department')
        lab_number = request.data.get('lab_number')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        professor = Professor.objects.create(name=name, department=department, lab_number=lab_number, user=user)


        return Response({"message": "교수 계정 생성 성공"})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)

        # 사용자의 역할(role)에 따라 다른 메시지를 반환합니다.
        if hasattr(user, 'student'):
            return Response({'role': '학생', 'refresh': str(refresh), 'access': str(refresh.access_token)})
        elif hasattr(user, 'professor'):
            return Response({'role': '교수', 'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({'role': '알 수 없음', 'refresh': str(refresh), 'access': str(refresh.access_token)})
    else:
        return Response({"message": "로그인 실패. 유효하지 않은 사용자명 또는 비밀번호."})


@login_required
def profile(request):
    return render(request, 'profile.html')


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


def login2_view(request):
    return render(request, 'login2.html')


@csrf_exempt
def professor_list(request):
    if request.method == 'GET':
        professors = Professor.objects.all()  # 데이터베이스에서 모든 교수님 정보를 조회합니다.
        professor_list = []
        for professor in professors:
            professor_data = {
                'id': professor.id,
                'name': professor.name,
                'department': professor.department,
                'email': professor.email,
                'photo': str(professor.photo),
                'phone': professor.phone_number,
                'lab_number': professor.lab_number,
            }
            professor_list.append(professor_data)

        return JsonResponse(professor_list, safe=False)
    elif request.method == 'POST':
        # POST 요청 처리 로직을 여기에 작성하세요.
        # 필요에 따라서 프론트엔드에 응답을 보내거나 다른 처리를 수행할 수 있습니다.
        return JsonResponse({'message': 'POST 요청이 정상적으로 처리되었습니다.'})


def delete_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    professor.delete()
    return HttpResponse("교수 삭제 완료")
