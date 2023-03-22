from rest_framework import authentication, permissions, generics
from .serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
