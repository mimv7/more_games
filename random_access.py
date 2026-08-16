import random

word = 'abc'
print(word)
hight = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low,hight)
    print(f'word {position} {word[position]}')