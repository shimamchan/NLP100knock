import gzip
import json
import re

file = 'jawiki-country.json.gz'

def extract():
    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

for line in extract():
    c_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if c_line is not None:
        print(c_line.group(1))