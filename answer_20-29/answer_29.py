import re
import gzip
import json
import requests

file = 'jawiki-country.json.gz'
dic = {}

def extract():
    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text'].split('\n')

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict


def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\[.*?\]", r"", str)
    return str

for line in extract():
    temp_line = re.search("^\|(.*?)\s=\s(.*)", line)
    if temp_line is not None:
        dic[temp_line.group(1)] = remove_markup(temp_line.group(2))

url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(dic[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()

print(json_search(json_data)["url"])