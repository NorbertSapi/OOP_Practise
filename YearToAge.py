# import class Age
from Age import Age


# get data from input: name and birth_year
name = input("What is your name? ")
print("Hi %s nice to meet you. " % name)

birth_year: str = input("When were you born? ")
print("You were born in %s " % birth_year)


# instantiating Age object
user1 = Age(name, birth_year)

# calling calculate() method
user1.calculate_age(birth_year)
