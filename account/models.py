from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,password = None):
        if not email:
            raise ValueError("The user must have an email")
        if not username:
            raise ValueError("The user must have an username")
        if not first_name:
            raise ValueError("The user must have a name")

        user = self.model(email = self.normalize_email(email),username = username,first_name = first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,first_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserRole(models.Model):
    name = models.CharField(max_length = 100)

class Account(AbstractBaseUser):
    email        = models.EmailField(max_length = 100,null = False,unique = True)
    username     = models.CharField(max_length=100,null = False,unique = True)
    date_joined  = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now_add=True)
    is_staff     = models.BooleanField(default = False)
    is_admin     = models.BooleanField(default = False)
    is_active    = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    first_name   = models.CharField(max_length=100,null = False)
    last_name    = models.CharField(max_length=100,null = True)
    password     = models.CharField(max_length=30,null = False)
    type         = models.ForeignKey(UserRole,null = False,on_delete = models.DO_NOTHING)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','password']

    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True