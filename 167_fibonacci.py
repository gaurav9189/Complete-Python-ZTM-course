
import pdb

pdb.set_trace()


def fib(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        temp = a
        a = b
        b = temp + b
        i += 1
        print(a)
        # print(b)


fib(5)
# #  0 1 1 2 3 5
# 0 1
# 1 1
# 1 2
# 2 3
# temp a b
# 0 1 2
# 1 2 3
# 2

# a b c
# temp = a
# a = b
# b = temp + b


def fib1(num):
    a = 0
    b = 1
    for i in range(num):
        temp = a
        a = b
        b = temp + b
        yield a


for num in fib1(10):
    print(num)
