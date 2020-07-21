from django.db import models

# Create your models here.

class Net(models.Model):

    net_name = models.CharField(max_length=50)

    def __str__(self):
        return "[" + self.net_name + "]"