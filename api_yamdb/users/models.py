from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    ]

    confirmation_code = models.CharField(
        max_length=100,
        blank=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Введите адрес эл.почты',
        unique=True
    )
    bio = models.TextField(
        verbose_name='О пользователе',
        help_text='Расскажите о себе',
        blank=True,
        null=True
    )

    role = models.CharField(
        'Роль пользователя',
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default=USER,
        blank=True,
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        confirmation_code = default_token_generator.make_token(
            instance
        )
        instance.confirmation_code = confirmation_code
        instance.save()
