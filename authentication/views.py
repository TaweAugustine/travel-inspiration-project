from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .serializers import (UserSerializer,
                        TokenObtainPairSerializer,
                        CustomUserSerializer
                        )

class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class CustomUserView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user.user
