from django.db import models, transaction
import re, threading
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

	def __str__(self):
		return self.request_line

	def __init__(self, tokens):
		self.ip_address = tokens[0]
		self.rfc_id = tokens[1]
		self.user_id = tokens[2]
		self.date_time = tokens[3]
		self.request_line = tokens[4]
		self.http_status = tokens[5]
		self.num_bytes = tokens[6]


class LogParserThread(threading.Thread):
	file_url = None

	def __init__(self, file_url):
		self.file_url = file_url

	def parse_line(line):
		regex = '([(\d\.)]+) ([A-Za-z\-]+) ([A-Za-z\-]+) \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'
		line = line.strip()
		match_obj = re.match(regex, line)
		if match_obj == None:
			return None
		else:
			tokens = match_obj.groups()
			return tokens

	def run(self):
		parsed_logs = []
        with open(uploaded_file_url, 'r') as log_file:
            for line in log_file:
                tokens = self.parse_line(line)
                if tokens == None:
                	continue
                parsed_logs.append(ParsedLog(tokens))

        ParsedLog.objects.bulk_create(parsed_logs)
