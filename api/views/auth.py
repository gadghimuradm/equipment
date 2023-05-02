from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CustomAuthTokenSerializer


class CustomAuthToken(ObtainAuthToken):
    """ Login """
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """ Logout """

    def get(self, *args, **kwargs):
        self.request.user.auth_token.delete()
        logout(self.request)
        return Response(status=status.HTTP_200_OK)
