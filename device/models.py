from django.db import models

# Create your models here.
from net.models import Net
class Device(models.Model):

    STATUS = ((0,'离线'), (1,'在线'))
    device_id = models.CharField(max_length=50)
    device_name = models.CharField(max_length=50)
    is_active = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    mac_addr = models.CharField(max_length=20)
    Longitude = models.CharField(max_length=20)
    Latitude = models.CharField(max_length=20)
    info = models.CharField(max_length= 200)
    net = models.ForeignKey(Net, null=True, blank=True, on_delete=models.SET_NULL)

