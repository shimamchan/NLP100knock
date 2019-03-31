file = 'hightemp.txt'

with open(file) as data, \
        open('col1.txt', mode = 'w') as col1_file, \
        open('col2.txt', mode = 'w') as col2_file:
    for line in data:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')