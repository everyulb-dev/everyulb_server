# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import CustomUser
from .serializer import CustomUserSerializer
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework_jwt.views import obtain_jwt_token


class CustomUserLogin(APIView):
	def post(self, request, format=None):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response(
                obtain_jwt_token({
                    "username" : username, "password" : password
                })
            )
		else:
			return Response({ 'Token': None })

class CustomUserLogout(APIView):
	def get(self, request, format=None):
		logout(request)



class CustomUserRegister(APIView):
    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(username=username, password=password)
        user.is_staff = True
        user.save()

        if authenticate(request, username=username, password=password) is not None:
            return Response({"Status" : True})
        else:
            return Response({"Status" : False})
