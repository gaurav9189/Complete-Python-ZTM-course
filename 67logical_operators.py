# Using logical operators

is_magician = False
is_expert = True

# Check if magicicna and expert 'you are a master magician'
# Check if magician but not expert: 'u are getting there
# if not magician: you need powers


def check_magic(magic, expert):
    if magic and expert:
        print('you are a master magician')
    elif magic and not expert:
        print('you are getting there')
    else:
        print('you need powers')


print(check_magic(magic=True, expert=True))
print(check_magic(magic=False, expert=True))
print(check_magic(magic=False, expert=False))
print(check_magic(magic=True, expert=False))

# li = [10, 20, 30, 40, 10, 50]
# greatest = 0
# for i in li:
#     if i > greatest:
#         greatest = i
#     # else:
#     #     break
#     print(f'let\'s check this value of greatest {greatest}')
