from time import time


def mydecorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}')
    return wrapper


@mydecorator
def calc(num):
    for i in range(100000000):
        i*num


'''
Explanation of the code-
passing the func as an input to the decorator which then returns the wrapper
the second step then passess the argument to the wrapper
'''
# a = mydecorator(calc)
# a(10)

# calc(4)

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1['valid']:
            print('you\'re allowed')
            fn(*args, **kwargs)
        else:
            print('not allowed')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
