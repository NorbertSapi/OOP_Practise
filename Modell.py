# This is the modell of the employee.


class Modell:
    pass

    def __init__(self, name, id, age, department):
        self.name = name
        self.id = id
        self.age = age
        self.department = department


    def __str__(self):
        return "Employee name is %s, id number is %s, age of the employee is %d, and the department is %s." % (
            self.name, self.id, self.age, self.department)
