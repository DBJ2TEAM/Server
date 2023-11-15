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



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer



# 학생 정보 임의로 만들기
@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        department = request.POST.get('department')
        student_id = request.POST.get('student_id')
        year = request.POST.get('year')

        user = User.objects.create_user(username=username, password=password, email=email)
        student = Student.objects.create(name=name, department=department, student_id=student_id, year=year, user=user)

        return HttpResponse("학생 계정 생성 성공")
    else:
        return render(request, 'login.html')
# 교수 모델 만들기인데 프론트와 협의 후 생성예정
@csrf_exempt
def register_professor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        department = request.POST.get('department')
        lab = request.POST.get('lab')

        user = User.objects.create_user(username=username, password=password, email=email)
        professor = Professor.objects.create(name=name, department=department, lab=lab, user=user)

        return HttpResponse("교수 계정 생성 성공")
    # 로그인 하기
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse("로그인 성공")
        else:
            return HttpResponse("로그인 실패. 유효하지 않은 사용자명 또는 비밀번호.")
    else:
        return render(request, 'login.html')  # 로그인 폼 출력
    
 # 로그인됐는지 프로필 페이지에서 확인할라고 만듦   
@login_required
def profile(request):
    return render(request, 'profile.html')
# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('/')