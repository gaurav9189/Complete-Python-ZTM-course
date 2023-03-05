# Functional programming
'''
# Data and function should interact with each other without creating a side effect
le'ts create a function which multiplies a list and returns it
'''


from functools import reduce


def mult(li):
    newli = [i*2 for i in li]
    return newli


li = [123, 123, 123, 4, 5, 12]

print(f'{mult(li)} this is function based result')
print(f'{[*map(lambda i: i*2, li)]} this is using map')

'''
Let's talk about filters next.
Filter function returns values that are True, unlike map which will return the same number of
items as the input items

'''


def odd_num(item):
    return item % 2 != 0


print(f'{list(filter(odd_num, li))} this is the op for filter')


li1 = [1, 3, 4, 5]
li3 = [1, 6, 8, 0]
# Zip function
print(f'{list(zip(li, li1, li3))} thi is the output of zip')

# reduce. BAsically uses a counter/accumulator like var which helps then reduce the output


def accu(acc, item):
    print(acc, item)
    return acc + item


print(f'{reduce(accu, li1, 0)} this is an output for reduce function')


'''
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
'''
my_pets = ['sisi', 'bibi', 'titi', 'carla']
scores = [73, 20, 65, 19, 76, 100, 88]
my_numbers = [5, 4, 3, 2, 1]


def capital(my_pets):
    return my_pets.capitalize()


def score(scores):
    if scores >= 50:
        return scores


def combined(acc, total):
    return acc + total


print(f'{[*map(capital, my_pets)]} is the output of map exercise')
print(f'{[*map(lambda i: i.capitalize(), my_pets)]} is the output of map exercise using lambda')

print(f'{[*filter(score, scores)]} is the output of filter exercise')
print(f'{[*filter(lambda x: x > 50, scores)]} is the output of filter exercise using lambda')

print(f'{reduce(combined, scores + my_numbers)} is the output of reduce exercise')
print(f'{reduce(lambda x, y: x + y, scores + my_numbers)} is the output of reduce exercise')
