def greet():
    return 'Hello Gaurav'


def func(greet):
    print(greet())


a = func(greet)
print(a)
# HRO is highest order function which either takes a function or returns one


def some_fun():
    def another_fun():
        return 'HRO rocks'
    return another_fun


b = some_fun()
print(b())
# Decorator pattern below


def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func


@my_decorator
def hello():
    print('Hi From Edinburgh')


# @my_decorator
def bye():
    print('Bye From Edinburgh')


hello()
bye()

# What's happening under the hood- decorator will pass the underlying function to itself as an argument

# a = my_decorator(hello)
# a()
