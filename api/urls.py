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
    path('register_student/', register_student, name='register_student'),
    path('register_professor/', register_professor, name='register_professor'),
]
