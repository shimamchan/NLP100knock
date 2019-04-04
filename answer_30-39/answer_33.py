import module as m

m.parse_neko()

nouns = set()
nouns_test = []
lines = m.neco_lines()
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
            nouns.add(morpheme['surface'])
            nouns_test.append(morpheme['surface'])

print(sorted(nouns, key=nouns_test.index))
