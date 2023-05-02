from uuid import uuid4

from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from api.managers.auth import CustomUserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    """
    User model
    """
    username, user_permissions, groups = None, None, None

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    login = models.CharField('Логин', max_length=100, unique=True,
                             help_text='Логин', null=False)
    email = models.EmailField('E-mail', help_text='Введите Email', validators=[validate_email])
    is_superuser = models.BooleanField(
        'Статус суперпользователя', default=False,
        help_text='Право на редактирование моделей связанных с ролями и '
                  'пользователями',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
