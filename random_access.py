import random

word = 'abc'
print(word)
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randint(low,high - 1)
    print(f'word {position} world[{word[position]}]')

