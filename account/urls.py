from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from account.views import CustomUserModelViewSet,UserRetrieveUpdateDestroyAPIView

router = routers.DefaultRouter()
#get data from all users
router.register(r'users',CustomUserModelViewSet)

urlpatterns = [
  url(r'^api/', include(router.urls)),
  #regresa informacion del usuarios loggeado
  url(r'data/',UserRetrieveUpdateDestroyAPIView.as_view(), name="user-data"),
  
]
