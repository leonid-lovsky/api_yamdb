from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser

from .serializers import RegistrationSerializer, GetTokenSerializer


class GetTokenAPIView(APIView):
    """
    Описание класса. # TODO
    """
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            user = CustomUser.objects.get(username=data['username'])
        except CustomUser.DoesNotExist:
            return Response(
                {'username': 'Пользователя с таким именем не существует'},
                status=status.HTTP_404_NOT_FOUND
            )
        if data.get('confirm_code') == user.confirm_code:
            token = RefreshToken.for_user(user).access_token
            return Response(
                {'token': str(token)},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'conirm_code': 'Предоставлен неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )


class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет)
    доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['mail_subject'],
            body=data['email_info'],
            to=[data['to_email']]
        )
        email.send()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        email_info = (
            f'Здравствуйте {user.username}'
            f'\nДля заверешения регистрации вам необходимо указать проверочный код:'
            f'{user.confirm_code}'
        )
        data = {
            'email_info': email_info,
            'to_email': user.email,
            'mail_subject': 'Код подтверждения для регистрации на сайте YaMDB'
        }
        self.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
