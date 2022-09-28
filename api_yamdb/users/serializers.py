from rest_framework import serializers

from .models import User
from api_yamdb import settings


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    class Meta:
        model = User
        fields = ['email', 'username']

    def validate_username(self, value):
        if value == settings.RESERVED_NAME:
            raise serializers.ValidationError(settings.MESSAGE_FOR_RESERVED_NAME)
        return value


class GetTokenSerializer(serializers.ModelSerializer):
    """ Сериализация выдачи пользователю токена. """
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']
