import random

maxn = 5

n = random.randint(1, maxn)

print('Welcome to guess the number game is done by L.RISHIWARDHAN')

print('Guess the number from 1 to %d' % maxn)

guess = ('6')

while guess != n:

    guess = int(input('new try: '))

    if guess > n:

        print('Too high')

    if guess < n:

        print('Too low')

print('Congratulations, you won!')

print('you did it')

print ('if you did it in the first try you will be added in the master of guess the numer game ')

print ('master of the game')

print ('RISHIWARDHAN')
