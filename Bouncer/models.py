from django.db import models, transaction
import re


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

	def __str__(self):
		return self.request_line

	def parse_line(self, line, regex):
		line = line.strip()
		tokens = re.match(regex, line).groups()
		return tokens

	def __init__(self, log):
		regex = '([(\d\.)]+) ([A-Za-z\-]+) ([A-Za-z\-]+) \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'
		tokens = self.parse_line(log, regex)

		self.ip_address = tokens[0]
		self.rfc_id = tokens[1]
		self.user_id = tokens[2]
		self.date_time = tokens[3]
		self.request_line = tokens[4]
		self.http_status = tokens[5]
		self.num_bytes = tokens[6]
