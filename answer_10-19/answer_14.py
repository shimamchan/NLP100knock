file = 'hightemp.txt'

n = int(input())

with open(file) as data:
    for i, line in enumerate(data):
        if i >= n:
            break
        print(line.rstrip())