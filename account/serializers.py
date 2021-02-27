from rest_framework import serializers
from .models import Account
from rest_framework.authtoken.models import Token

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username','email','password','first_name',"date_joined")
        extra_kwargs ={'password':{'write_only':True}}

    def create(self,validated_data):
        user = Account(email=validated_data['email'],username=validated_data['username'],first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        return user