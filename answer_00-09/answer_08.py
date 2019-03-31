def cipher(text):
    b = ''
    for c in text:
        b += chr(219 - ord(c)) if c.islower() else c
    return b

a = 'The train came out of the long tunnel into the snow country. The earth lay white under the night sky. The train pulled up at a signal stop.'

result1 = cipher(a)
result2 = cipher(result1)

print(result1)
print(result2)
