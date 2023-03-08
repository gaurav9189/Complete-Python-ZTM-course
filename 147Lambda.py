# Lambda function
'''
lambda param: action(param)
'''
# square
item = [1, 2, 3, 4, 5]
print([*map(lambda x: x**2, item)])

# List sorting
# Here we'll end up using list method of sort and understand how it works
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[-1])
print(a)
a.sort()

# List comprehensions-
'''
[expr for var in iter conditiona]
expr such as 2*x
var suc as x
condition such as if x % 2 ==0
'''
li = [10, 30, 50, 10, 40, 60, 100, 12, 123, 21, 4]
new_li = [x for x in li if x % 10 == 0]
print(new_li)
