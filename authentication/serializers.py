from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import generics

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TokenObtainPairSerializer(serializers.Serializer):
    username_field = User.USERNAME_FIELD
    default_error_messages = {
        'no_active_account': 'L\'utilisateur doit activer son compte avant de se connecter.',
        'invalid_credentials': 'Les informations de connexion fournies sont invalides. Veuillez réessayer.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = serializers.CharField(
            style={'input_type': 'password'},
            trim_whitespace=False
        )

    def validate(self, attrs):
        user = authenticate(**{
            self.username_field: attrs[self.username_field],
            'password': attrs['password']
        })

        if user:
            if not user.is_active:
                raise serializers.ValidationError(
                    self.error_messages['no_active_account'],
                    code='no_active_account',
                )

            refresh = self.get_token(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return data

        raise serializers.ValidationError(
            self.error_messages['invalid_credentials'],
            code='invalid_credentials',
        )
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'