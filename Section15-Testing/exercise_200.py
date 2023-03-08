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
            return 'Wrong Range'
        elif guess == answer:
            # print(f'you\'ve guessed it')
            return 1
            # break
        else:
            if count > 10:
                print('you\'ve lost the game')
                return 'Lost'
            print(f'Not there yet, try again ans was {answer}')
            return 'Again'
    except:
        print('Something is not right')


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
        elif result == 'Lost' or result == 'Wrong Range':
            print('Lost the game')
            break
        else:
            print(f'i am count:{count}')
            count += 1


# rand(item)
