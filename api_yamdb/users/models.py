from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    ]

    bio = models.TextField(
        'Биография',
        blank=True,
    )

    confirm_code = models.CharField(
        max_length=100,
        blank=True
    )

    role = models.CharField(
        'Роль пользователя',
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default=USER,
        blank=True,
    )


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        confirm_code = default_token_generator.make_token(
            instance
        )
        instance.confirm_code = confirm_code
        instance.save()
