# import class Age
from Age import Age


# get data from input: name and birth_year
name = input("What is your name? ")
print("Hi %s nice to meet you. " % name)

username = input("Enter your username: ")
print("Username: %s " % username)
pass_word = input("Enter your password")
length_password = int(len(pass_word))

print("Your password is {} and your password is {} character long. ".format(pass_word, length_password))


birth_year: str = input("When were you born? ")
print("You were born in %s " % birth_year)


# instantiating Age object
user1 = Age(name, birth_year)

# calling calculate() method
user1.calculate_age(birth_year)
