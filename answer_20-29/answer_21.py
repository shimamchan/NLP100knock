import gzip
import json

file = 'jawiki-country.json.gz'

def extract():
    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text'].split('\n')

for line in extract():
    if 'Category' in line:
        print(line)