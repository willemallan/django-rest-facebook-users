from django.db import models


class Client(models.Model):
    facebook_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
            

    class Meta:
        ordering = ('name',)