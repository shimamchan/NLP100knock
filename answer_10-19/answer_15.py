file = 'hightemp.txt'

n = int(input())

if n > 0:
    with open(file) as data:
        lines = data.readlines()
    for line in lines[-n:]:
        print(line.rstrip())