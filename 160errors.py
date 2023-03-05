def calc(num1, num2):
    try:
        return num1 / num2
    except(TypeError, ZeroDivisionError, ValueError) as err:
        print(f'Something is wrong- {err}')


# calc(1, '1')

#
while True:
    try:
        age = int(input('Enter you age: '))
        10/age
    except ValueError as err:
        print('Value error')
        continue  # you won't get broken out of the loop
    except ZeroDivisionError as err:
        print('Zero is not allowed')
        break
    else:
        print('This is great input')
        break
    finally:  # This gets executed on all occasions
        print('you are now done')
