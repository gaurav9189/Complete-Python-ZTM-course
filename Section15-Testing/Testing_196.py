# Each testing code is to test features or development work
def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        return ('Please enter a number')
    except ValueError as err:
        return err
