# OOP
from Skills import Skills
from Modell import Modell

worker1 = Modell("Jo", "110147", 25, "Pick")
print(worker1.name)
print(worker1.id)
print(worker1.age)
print(worker1.department)

# two ways to call str method from class Modell
Modell.str(worker1)
worker1.str()


# instantiating the skills class
person1 = Skills("True", "Pack")
person2 = Skills("True", "Pick")
print(person1.new_hire)
print(person1.where_department)

# calling development method from class Skills
person1.development(True, True, True)
person2.development(False, True, False)


# this is a method which tells you if the training is in progress
# method from Main class
def development(learning):
    if learning:
        print("method from Main class")
        print("learning in progress")
    else:
        return False


# calling the development method from Main class
development("True")

print("Hello-GitHub-World")
