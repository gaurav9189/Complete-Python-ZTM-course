
total = 0
##########################
# def count():
#     print(total) # This will print the value of total as the interpretter finds it from the global scope
#     # after not being able to find it in the local scope
#     # total += 1 -> this will error because the total variable doens't exist in the local scope and the func can't modify the global scope like this
################################


# def count():
#     global total
#     total += 1
#     return total

# count()
# count()
# print(count())

# print(f'the global total value is- {total} ')
# So if you see the global scope is also modified with this approach

# A better approach would be-


def count(total):
    total += 1
    return total


print(count(count(total)))
print(total)
