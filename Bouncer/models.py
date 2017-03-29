from django.db import models, transaction
import re


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


test_log = '64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846'
parsed = ParsedLog(test_log)
print parsed
