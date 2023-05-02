from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomAuthTokenSerializer(serializers.Serializer):
    """ Authtoken serializer """
    login = serializers.CharField(
        label="Логин",
        required=False
    )
    password = serializers.CharField(
        label="Пароль",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    class Meta:
        model = User
        fields = ("login", "password")

    def validate(self, attrs):
        """ Validate data """
        login = attrs.get('login')
        password = attrs.get('password')

        if login and password:
            user = authenticate(request=self.context.get('request'),
                                login=login, password=password)

            if not user:
                msg = 'Неверный логин или пароль'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Введите логин и пароль'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
