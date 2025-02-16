import sys

sys.path.append('..')
from django.contrib.auth import get_user_model
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import UserSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from posts.permissions import IsOwnerOrReadOnly

# Create your views here.

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    """
    post:
        Create new user instance. Returns username, email of the created user.

        parameters: [username, email, password]
    """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the detail of a user instance

        parameters: [id]

    put:
        Update the detail of a user instance

        parameters: [id, username, email, password]

    delete:
        Delete a user instance

        parameters: [id]
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserListAPIView(ListAPIView):
    """
    get:
        Returns list of all exisiting users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
