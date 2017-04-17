from django.db import models, transaction
from django.contrib.auth.models import User



class Login(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length = 40)


# class to store Apache log files using Common Log Format
class ParsedLog(models.Model):
	ip_address = models.CharField(max_length=39)
	rfc_id = models.CharField(max_length=39)
	user_id = models.CharField(max_length=39)
	date_time = models.CharField(max_length=29)
	request_line = models.TextField()
	http_status = models.CharField(max_length=3)
	num_bytes = models.IntegerField(blank=True)
