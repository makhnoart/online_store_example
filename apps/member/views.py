from django.shortcuts import render
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from apps.member.models import User
from apps.member.serializers import (UserSignUpSerializer,
                                     UserSignInSerializer, UserDetailSerializer,
                                     SuperUserDetailSerializer,
                                     UserEmailConfirmSerializer)


class SignUpView(APIView):

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SignInView(APIView):

    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserDatailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = UserDetailSerializer(request.user, context={'user': request.user})
        return Response(serializer.data)


class UserEmailConfirmView(APIView):
    def get(self, request, key):
        serializer = UserEmailConfirmSerializer(data={
            'key': key
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
