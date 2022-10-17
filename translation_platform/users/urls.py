from django.urls import path, include
from rest_framework import routers
from .views import RegisterAPIView, AuthView

router = routers.SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()), #회원가입하기
    path("auth/", AuthView.as_view()), #로그인하기
]