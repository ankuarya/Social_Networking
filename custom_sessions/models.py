from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CustomSessions(models.Model):
    username = models.CharField(max_length=255)
    login_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
