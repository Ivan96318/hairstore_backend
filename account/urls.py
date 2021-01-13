from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
  url(r'^api/', include(router.urls)),
]
