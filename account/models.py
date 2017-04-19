from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Models

# 
@python_2_unicode_compatible
class Log(models.Model):
    log_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    log_owner = models.ForeignKey(User, null = True)
    def __str__(self):
        return self.log_text
