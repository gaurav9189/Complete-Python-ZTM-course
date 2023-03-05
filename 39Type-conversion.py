# Writing a simple function to take an input of the age and display it

def my_age(yr):
    age = 2023 - yr
    return(f'Your age is {age}')


year = input('What\'s your birth year: ')
# Make sure you type convert your input as it is string!
response = my_age(int(year))  # Type convert, also the type of response is str!
print(response)
