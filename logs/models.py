# -*- coding: utf-8 -*-
from django.db import models

LEVEL_CHOICES = (
    ('DEBUG', 'DEBUG'),
    ('INFO', 'INFO'),
    ('WARNING', 'WARNING'),
    ('ERROR', 'ERROR'),
    ('CRITICAL', 'CRITICAL')
)


class Log(models.Model):
    name = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    message = models.TextField()
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
    create = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = u'Log'
        verbose_name_plural = u'Logs'
        
    def __unicode__(self):
        return "%s" % self.name
        