import re
import pdb


# pdb.set_trace()


def pw_check(password):
    try:
        pattern = re.compile(r"([\w@#%$]){7,}\d$")
        p1 = pattern.fullmatch(password)
        # print(p1)
        if p1:
            print('Your password was good')
            return(f'your password: {password} is set')
        print('Wrong password try again')
    except:
        print('Something was wrong')


password = input('Please enter your password with min 8 chars and %$#@: ')
print(pw_check(password))
