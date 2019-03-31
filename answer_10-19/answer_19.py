from itertools import groupby

file = 'hightemp.txt'

lines = open(file).readlines()
prefs = [line.split('\t')[0] for line in lines]

prefs.sort()
result = [(pref, len(list(group))) for pref, group in groupby(prefs)]
result.sort(key=lambda pref: pref[1], reverse=True)

for pref in result:
    print('{pref}:{count}'.format(pref=pref[0], count=pref[1]))