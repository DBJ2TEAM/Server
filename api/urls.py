from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('User', views.UserViewSet) #itemviewset 과 item이라는 router 등록

urlpatterns = [
    path('', include(router.urls))
]