import random
print(__name__)


def guess_game(num):
    count = 0
    while True:
        val = int(input(f'Enter the number between 1-{num}: '))
        if val > num or val < 1:
            print('Out of range')
            break
        elif val == random.randrange(10):
            print(f'you guessed it in {count} times')
            break
        count += 1
        print('Wrong guess, try again')
        continue
