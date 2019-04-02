import gzip
import json
import re

file = 'jawiki-country.json.gz'

def extract():
    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text'].split('\n')

for line in extract():
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2), len(section_line.group(1)) - 1)