file = 'hightemp.txt'
with open(file) as data:
    pref = set()
    for line in data:
        cols = line.split('\t')
        pref.add(cols[0])

for n in pref:
    print(n)