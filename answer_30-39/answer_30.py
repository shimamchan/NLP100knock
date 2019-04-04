import MeCab
f = 'neko.txt'
_f = 'neko.txt.mecab'


def parse_neko():
    with open(f) as data_file, \
            open(_f, mode='w') as out_file:

        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neco_lines():
    with open(_f) as f_parsed:

        morphemes = []
        for line in f_parsed:

            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration
            res_cols = cols[1].split(',')

            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []


parse_neko()

lines = neco_lines()
for line in lines:
    print(line)
