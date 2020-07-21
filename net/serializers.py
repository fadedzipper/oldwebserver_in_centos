from rest_framework import serializers
from net import models

class NetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Net
        fields = ['id', 'net_name']








