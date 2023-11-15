from rest_framework import viewsets
from .models import Student, Professor
from .serializers import StudentSerializer, ProfessorSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Professor
from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


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
        lab = request.data.get('lab')

        user = User.objects.create_user(username=username, password=password, email=email)
        professor = Professor.objects.create(name=name, department=department, lab=lab, user=user)

        return Response({"message": "교수 계정 생성 성공"})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
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
