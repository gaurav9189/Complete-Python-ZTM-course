# List methods

some_list = ['apple', 'mango', 'grapes']

# methods in list that don't return, or return None type

out1 = some_list.reverse()
out2 = some_list.append('oranges')
out3 = some_list.insert(4, 'kiwis')

# Wouldn't return anything
print(out1)
print(out2)
print(out3)

# Scroll down to see the answers!
# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {'age': 34,
                'username': 'Gaurav',
                'is_active': True,
                'weapons': 'Katana',
                'clan': 'Novacoders'}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())
# 3 Add a new weapon to your user
user_profile.update({'weapons': ['Katana', 'sword']})
print(user_profile)
# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update([('isbanned', False)])
print(user_profile)

# 5 Ban the user by setting the previous key to True
user_profile.update(isbanned=True)
print(user_profile)


# the update method takes these inputs-
#  Either a dictionary to update elements or a list of tuples or directly keyvalue arguments as k=v
# I read the realpython documentation and tried understanding the help doc on this method
