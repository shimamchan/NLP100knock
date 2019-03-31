import random

def typoglycemia(text):
    result = []
    for word in text.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0] + ''.join(chr_list) + word[-1])

    return ' '.join(result)

a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(a))