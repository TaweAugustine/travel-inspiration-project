
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import CustomUserView
from django.urls import path
from .views import RegistrationView, ObtainTokenPairView


urlpatterns = [
 path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
 path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
 path('api/register/', RegistrationView.as_view(), name='register'),
 path('api/users/', CustomUserView.as_view(), name='users'),

]


