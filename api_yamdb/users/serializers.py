from rest_framework import serializers

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    class Meta:
        model = CustomUser
        fields = ['email', 'username']


class GetTokenSerializer(serializers.ModelSerializer):
    """ Сериализация выдачи пользователю токена. """

    class Meta:
        model = CustomUser
        fields = ['username', 'confirm_code']
