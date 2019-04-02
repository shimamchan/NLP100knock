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
    file_line = re.search(u"(File|ファイル):(.*?)\|", line)
    if file_line is not None:
        print(file_line.group(2))