from django.urls import path, include
from rest_framework_simplejwt.views import (
TokenObtainSlidingView,
TokenRefreshSlidingView
)
from .viewset import RegisterUser
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
path('register/',RegisterUser.as_view(), name='register'),
path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]