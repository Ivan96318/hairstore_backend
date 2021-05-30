from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from .serializers import AccountSerializer
from django.contrib.auth import get_user_model
from .models import Account
from django.core.paginator import Paginator
from utils.views import checkpaginator
from rest_framework.authtoken.models import Token

#customUser = get_user_model()

# Create accounts - this is good
'''
class AccountCreation(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AccountSerializer
'''
# Login api
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_object(self):
        return self.request.user

#get enlista todos los usuarios and post crea un nuevo usuario
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    #permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    '''
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    '''

    def get_queryset(self):
        checkpaginator(self)
        
        return self.queryset

    def create(self, request):
        try:
            user = Account.objects.create(email = request.data.get("email"),username = request.data.get("username"),is_admin = request.data.get("is_admin"),first_name = request.data.get("first_name"),last_name = request.data.get("first_name"))
            user.set_password(request.data.get("password"))
            user.save()
            Token.objects.create(user = user)
            return Response({'rs':'User Created Successfully','success':True})
        except Exception as error:
            return Response({'rs':'Error: {}'.format(error),'success':False})



