# NameError undefined variable
# Type error int and str
# Index error using Li
# Key error using dict
# try and except

import random
import pdb
# pdb.set_trace()


def rand(guess, answer, count=1):
    try:
        if (guess < 0 or guess > 10):
            print('Wrong range')
            return 0
        elif guess == answer:
            # print(f'you\'ve guessed it')
            return 1
            # break
        else:
            if count > 10:
                print('you\'ve lost the game')
                return 0
            print(f'Not there yet, try again ans was {answer}')
            return 2
    except:
        print('Something is not right')


# The below statement is necessary because the testing starts running the game itself
if __name__ == '__main__':
    count = 1
    ans = random.randint(1, 10)
    while True:
        ans = random.randint(1, 10)
        item = int(input('Enter your guess: '))
        result = rand(item, ans, count)
        if result == 1:
            print(f'You guessed it with {count} times!')
            break
        elif result == 0:
            print('Lost the game')
            break
        else:
            print(f'i am count:{count}')
            count += 1


# rand(item)
