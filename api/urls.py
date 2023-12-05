from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    login_view, LogoutView, RegisterStudentView, RegisterProfessorView, login2_view,
    professor_list, delete_professor, refresh_token
)
from rest_framework.authtoken.views import obtain_auth_token
from .views import StudentAppointmentViewSet, ProfessorAppointmentViewSet

router = DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('professors', views.ProfessorViewSet)

router.register(r'student-appointments', StudentAppointmentViewSet, basename='student-appointment')
router.register(r'professor-appointments', ProfessorAppointmentViewSet, basename='professor-appointment')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('register_student/', RegisterStudentView.as_view(), name='register_student'),
    path('register_professor/', RegisterProfessorView.as_view(), name='register_professor'),
    path('login/', login_view, name='login'),
    path('login2/', login2_view, name='login2'),
    path('refresh_token/', refresh_token, name='refresh_token'),
    path('profile/', views.profile, name='profile'),
    path('professors_list/', professor_list, name='professor-list'), # 교수님 정보 리스트
    path('api/professors/<int:professor_id>/delete/', delete_professor, name='delete_professor'),

]
