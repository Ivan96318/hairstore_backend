from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from account.views import AccountViewSet,UserRetrieveUpdateDestroyAPIView

router = routers.DefaultRouter()
#get data from all users - check
router.register(r'users',AccountViewSet)

urlpatterns = [
  url(r'^api/', include(router.urls)),
  #regresa informacion del usuarios loggeado - check
  url(r'data/',UserRetrieveUpdateDestroyAPIView.as_view(), name="user-data"),
]
