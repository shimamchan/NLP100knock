file = 'hightemp.txt'
count = 0

with open(file) as data:
    for line in data:
        count += 1

print(count)