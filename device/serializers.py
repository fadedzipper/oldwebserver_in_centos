from rest_framework import serializers
from device import models

class DeviceSerializer(serializers.ModelSerializer):

    is_active = serializers.IntegerField()
    class Meta:
        model = models.Device
        fields = ['id', 'device_id', 'device_name', 'is_active', 'status', 'mac_addr', \
                  'Longitude', 'Latitude', 'info', 'net']


    # def get_obj(self, obj):
    #     if obj.is_active == 0:
    #         return "离线"
    #     return "在线"




class DeviceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = ['is_active', 'Longitude', 'Latitude', 'net', 'info', 'is_active']


class DeviceUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'is_active']
