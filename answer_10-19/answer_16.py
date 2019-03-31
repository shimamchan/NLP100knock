import math

file = 'hightemp.txt'
n = int(input())

with open(file) as data:
    lines = data.readlines()

count = len(lines)
unit = math.ceil(count / n)

for i, offset in enumerate(range(0, count, unit), 1):
    with open('separate_{:02d}.txt'.format(i), mode = 'w') as out:
        for line in lines[offset:offset + unit]:
            out.write(line)
