from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Models

@python_2_unicode_compatible
# class to store Apache log files using Common Log Format
class ParsedLog(models.Model):
	owner = models.ForeignKey(User, null=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	ip_address = models.CharField(max_length=39)
	rfc_id = models.CharField(max_length=39)
	user_id = models.CharField(max_length=39)
	date_time = models.CharField(max_length=29)
	request_line = models.TextField()
	http_status = models.CharField(max_length=3)
	num_bytes = models.IntegerField(blank=True)

	def __str__(self):
		return self.request_line
