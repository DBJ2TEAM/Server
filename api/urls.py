from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import login_view,register_student, register_professor

router = DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('professors', views.ProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
