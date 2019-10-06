# OOP
from Skills import Skills
from Modell import Modell

worker1 = Modell("Jo", "11014771", 25, "Pick")
print(worker1.name)
print(worker1.id)
print(worker1.age)
print(worker1.department)

# !!! You have to fix this part!!!
worker1.__str__

# from Skills import Skills
# instantiating the skills class
person1 = Skills("True", "Pack")

print(person1.new_hire)
print(person1.where_department)


# this is a method which tells you if the training is in progress
def development(learning):
    if learning:
        print("learning in progress")
        # return True
    else:
        return False


# calling the development method
development("True")

print("Hello-GitHub-World")
