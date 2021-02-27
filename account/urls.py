from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from account.views import CustomUserModelViewSet,UserRetrieveUpdateDestroyAPIView

router = routers.DefaultRouter()
router.register(r'users',CustomUserModelViewSet)

urlpatterns = [
  url(r'^api/', include(router.urls)),
  url(r'data/',UserRetrieveUpdateDestroyAPIView.as_view(), name="user-data"),
  
]
