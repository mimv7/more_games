print(
"""
0   1   3   4   5   6
+---+---+---+---+---+
| p | i | z | z | a |
+---+---+---+---+---+
-5  -4  -3  -2  -1
"""
)
word = 'pizza'
start = None
while start != '':
    start = (input('start: '))
    if start:
        start = int(start)
        finish = int(input('finish: '))
        print(f'slice [{start}:{finish}] ')
        print(word[start:finish])
