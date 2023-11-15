from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import login_view, LogoutView, RegisterStudentView, RegisterProfessorView, login2_view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('professors', views.ProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('register_student/', RegisterStudentView.as_view(), name='register_student'),
    path('register_professor/', RegisterProfessorView.as_view(), name='register_professor'),
    path('login/', login_view, name='login'),
    path('login2/', login2_view, name='login2'),
    path('profile/', views.profile, name='profile'),
]
