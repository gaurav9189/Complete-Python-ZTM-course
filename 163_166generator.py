
from os import curdir


def some_func(num):
    return [i*2 for i in range(num)]


print(some_func(10))


def some_gen(num):
    for i in range(num):
        yield i


# yield returns a generator object
print(some_gen(10))
for i in some_gen(10):
    print(i)
# Now instead of a for loop i can use 'next' to iterate over this generator object

g = some_gen(10)
print(f'and the first iteration is {next(g)}')
print(f'and the second iteration is {next(g)}')

'''
Using iter for iterating. In this example i'm using try and except blocks to iterate over the iterable
Iterable being a list passed to the function. Next ensures that the next iterable is called from the
iterator.

'''


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])

'''
Using Classes to define my own data type. This time creating my own generator and undertand how
range really works and how it understands when to stop the iteration
'''


class MyGen():
    # current = 0

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        # self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            val = self.start
            self.start += 1
            return val
        raise StopIteration


gen = MyGen(11, 20)
for i in gen:
    print(i)
