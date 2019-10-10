# this is a small app to return your age from date of year
# create class Age


class Age:
    pass

    # initializing instance variables
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # this is a method which counts your age
    def calculate_age(self, year: object) -> object:
        age = 2019 - int(self.year)
        print(self.year)
        age = 2019 - int(self.year)
        print("You are %s years old" % age)
