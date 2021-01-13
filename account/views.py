from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import AccountSerializer

# Create your views here.
class AccountCreation(generics.CreateAPIView):
    serializer_class = AccountSerializer
