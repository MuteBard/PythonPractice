class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "%s %s %s" % (self.year, self.make, self.model)

car1 = Vehicle('Nissan', 'Leaf', 2015)
car1.print_info()
car2 = Vehicle('Honda', 'Civic', 2009)
car2.print_info()
