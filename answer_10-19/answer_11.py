file = 'hightemp.txt'

with open(file) as data:
    for line in data:
        print(line.replace('\t', ' '), end = '')