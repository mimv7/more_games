import random

toss = 0
heads = 0
tails = 0
while toss < 100:
    value_coins = random.randint(0,1)
    if value_coins == 0:
        heads += 1
    if value_coins == 1:
        tails += 1
    toss +=1

print(f'орлов выпало {heads},а решек {tails}')

