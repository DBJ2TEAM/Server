from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    login_view, LogoutView, RegisterStudentView, RegisterProfessorView, RegisterAssistantView, login2_view,
    professor_list, delete_professor, refresh_token
)
from rest_framework.authtoken.views import obtain_auth_token
from .views import StudentAppointmentViewSet, ProfessorAppointmentViewSet

router = DefaultRouter()
router.register('students', views.StudentViewSet)  # 학생 정보
router.register('professors', views.ProfessorViewSet)  # 교수 정보

router.register(r'student-appointments', StudentAppointmentViewSet, basename='student-appointment')  # 학생 예약 정보
router.register(r'professor-appointments', ProfessorAppointmentViewSet, basename='professor-appointment')  # 교수 예약 정보

urlpatterns = [
    path('', include(router.urls)),  # 라우터 URL 포함
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # 인증 토큰 얻기
    path('logout/', LogoutView.as_view(), name='api_logout'),  # 로그아웃
    path('register_student/', RegisterStudentView.as_view(), name='register_student'),  # 학생 계정 등록
    path('register_professor/', RegisterProfessorView.as_view(), name='register_professor'),  # 교수 계정 등록
    path('register_assistant/', RegisterAssistantView.as_view(), name='register_assistant'),  # 조교 계정 등록
    path('login/', login_view, name='login'),  # 로그인
    path('login2/', login2_view, name='login2'),  # 로그인2
    path('refresh_token/', refresh_token, name='refresh_token'),  # 토큰 새로고침
    path('profile/', views.profile, name='profile'),  # 프로필 정보
    path('professors_list/', professor_list, name='professor-list'),  # 교수 정보 리스트
    path('api/professors/<int:professor_id>/delete/', delete_professor, name='delete_professor'),  # 교수 계정 삭제
    path('professor-appointments/professor/<int:professor_id>', ProfessorAppointmentViewSet.as_view({'get': 'list_by_professor'}), name='professor-appointments-by-professor'),
]
