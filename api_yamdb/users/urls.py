from django.urls import path

from .views import RegistrationAPIView, GetTokenAPIView

namespace = 'users'

urlpatterns = [
    path(
        'signup/', RegistrationAPIView.as_view(), name='signup'
    ),
    path(
        'token/', GetTokenAPIView.as_view(), name='get_token'
    )
]
