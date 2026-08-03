import random

hidden_num = random.randint(1,100)
guess = False
count = 0
while count < 7  and not guess:
    supposed_num = int(input('input num - '))
    if supposed_num == hidden_num:
        print(f'guessed right! hidden num {hidden_num} ')
        guess = True

    elif supposed_num > hidden_num:
        print('less')
        count += 1
    elif supposed_num < hidden_num:
        print('more')
        count += 1
    else:
        print('error')
if not guess:
        print(f'attempts are over( hidden num {hidden_num}')
print(f'attepts - {count}')