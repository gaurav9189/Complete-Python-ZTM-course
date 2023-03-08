# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Bob', 10)
cat2 = Cat('Tim', 14)
cat3 = Cat('Gar', 12)
cat4 = Cat('Tom', 54)


def oldcat(*args):
    li = []
    for i in args:
        li.append(i.age)
    for c in args:
        if c.age == max(li):
            oldest = c.age
            return(f'im {c.name} and im {oldest} yrs')

    # return (f'im {c.name} and im {oldest} yrs')


print(oldcat(cat1, cat2, cat3, cat4))
