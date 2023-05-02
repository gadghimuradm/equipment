from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """ Custom user manager"""
    use_in_migrations = True

    def _create_user(self, **fields_kwargs):
        now = timezone.now()
        fields_kwargs['last_login'] = now
        fields_kwargs['date_joined'] = now
        fields_kwargs['email'] = self.normalize_email(fields_kwargs.get('email'))
        user = self.model(**fields_kwargs)
        user.set_password(fields_kwargs.get('password'))
        user.save()
        return user

    def create_user(self, **fields_kwargs):
        fields_kwargs['is_staff'], fields_kwargs['is_superuser'] = False, False
        return self._create_user(**fields_kwargs)

    def create_superuser(self, **fields_kwargs):
        fields_kwargs['is_staff'], fields_kwargs['is_superuser'] = True, True
        return self._create_user(**fields_kwargs)
