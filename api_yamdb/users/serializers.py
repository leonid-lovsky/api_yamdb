from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    class Meta:
        model = User
        fields = ['email', 'username']


class GetTokenSerializer(serializers.ModelSerializer):
    """ Сериализация выдачи пользователю токена. """
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']
