import sys
from random import randint

first = sys.argv[1]
second = sys.argv[2]
count = 0
while True:
    try:
        val = int(input(f'Guess a num between {first} and {second}: '))
        ans = randint(int(first), int(second))
        if val > int(second) or val < int(first):
            print('wrong range try again')
            break
        elif val == ans:
            print(f'you\'re a genius who took {count + 1} times to guess')
            break
        else:
            print(f'Wrong guess try again, {ans} was the ans')
            count += 1
            continue
    except ValueError as er:
        print(f'Must be a wrong input: {er}')
