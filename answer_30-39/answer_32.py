import module as m

m.parse_neko()

verbs = set()
verbs_test = []
lines = m.neco_lines()
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '動詞':
            verbs.add(morpheme['base'])
            verbs_test.append(morpheme['base'])

print(sorted(verbs, key=verbs_test.index))
