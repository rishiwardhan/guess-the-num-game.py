import random

maxn = 5
# you can add any number of the maxn 
n = random.randint(1, maxn)

print('Welcome to guess the number game is done by L.RISHIWARDHAN')
#you can add any name
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

print ('master of the game')

print ('RISHIWARDHAN')
