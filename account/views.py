from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from .serializers import AccountSerializer
from django.contrib.auth import get_user_model
from .models import Account
from django.core.paginator import Paginator
from utils.views import checkpaginator

customUser = get_user_model()

# Create accounts - this is good
class AccountCreation(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AccountSerializer

# create users simples
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_object(self):
        return self.request.user

#get enlista todos los usuarios and post crea un nuevo usuario
class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = customUser.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def get_queryset(self):
        checkpaginator(self)
        
        return self.queryset


