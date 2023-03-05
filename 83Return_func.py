# 83Return_func

# def first_fun(f1, f2):
#     print('im first fun')
#     def second_fun(s1, s2):
#         print('im 2nd func')
#         return f1+f2+s1+s2
#     return second_fun # We could also call the function here itself!

# this = first_fun(1, 2) #This will invoke the first fun and retunr the second_fun but 2nd won't be invoked
# print(this(2, 3)) #This will invoke the 2nd fun and returns all the elements sum for 1st and 2nd fun


def first_fun1(*f1):
    print('im first fun')

    def second_fun1(*f2):
        print('im 2nd func')
        print(f1, f2)
        # return f1+s1+s2

    return second_fun1(*f1)  # We could also call the function here itself!


# This will invoke the first fun and retunr the second_fun but 2nd won't be invoked
this1 = first_fun1(1, 2, 3)
# This will invoke the 2nd fun and returns all the elements sum for 1st and 2nd fun
print(this1)
