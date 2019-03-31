s1 = 'パトカー'
s2 = 'タクシー'
result = ''

for (a, b) in zip(s1, s2):
    result += a + b

print(result)