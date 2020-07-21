from django.urls import path,include,re_path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('', views.DeviceViewset)

urlpatterns = [

] + router.urls

