import re

# tokenize Apache log file


def parse_line(line):
    regex = '([(\d\.)]+) ([A-Za-z\-]+) ([A-Za-z\-]+) \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'
    line = line.strip()
    match_obj = re.match(regex, line)
    if match_obj == None:
        return None
    else:
        tokens = match_obj.groups()
        return tokens
