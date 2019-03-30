
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = []

for _s in s.split(' '):
    _s = _s.replace(",", "")
    result.append(len(_s))

print(result)