import gzip
import json
import re

file = 'jawiki-country.json.gz'
dic = {}

def extract():
    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text'].split('\n')

for line in extract():
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if temp_line is not None:
        dic[temp_line.group(1)] = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", re.sub(r"'{2,5}", r"", temp_line.group(2)))

for k, v in sorted(dic.items(), key=lambda x: x[1]):
    print(k, v)