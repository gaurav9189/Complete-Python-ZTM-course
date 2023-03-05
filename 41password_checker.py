# Define a function to take name and password
def len_password(name, password):
    # this helped me print * 'x' times, remember strings can do this
    plen = len(password)
    this = '*' * len(password)
    return(f'Hi {name} your password is {this} long, i.e {plen} char long')
    # The len expression can be added like this! so not just string variables but expressions
    # For readability i would add plen in the len expression!


name = input('Whats your name: ')
password = input('Whats your password: ')

response = len_password(name, password)
print(response)
