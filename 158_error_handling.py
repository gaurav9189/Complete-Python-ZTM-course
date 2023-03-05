# NameError undefined variable
# Type error int and str
# Index error using Li
# Key error using dict


# try and except

import random


def guess():
    count = 0
    try:
        while True:
            num = int(input('Let\'s enter a num: '))
            if (num < 0 or num > 30):
                print('Wrong range')
                break
            elif num == random.randint(1, 30):
                print(f'you\'ve guessed it and took {count} times')
                break
            else:
                count += 1
                if count > 10:
                    print('you\'ve lost the game')
                    break
                print('Not there yet, try again')
                continue
    except:
        print('Something\'s not right')

    else:
        print('You are a master')


# num = int(input('Let\'s enter a num:'))
guess()
