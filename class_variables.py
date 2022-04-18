import pdb

class Car:
    # Common for all objects. It belongs to class. It it class attribute
    wheels = 4

    def __init__(self):
        # Instance attributes
        self.engine = 'v4'
        self.model = ''
        self.issue_date = ''

    def log_me(self):
        print('model - ', self.model)
        print('wheels - ', Car.wheels)

c1 = Car()
c1.model = 'bmw'


c1.wheels = 7
c1.color = 'blue'
c1.log_me()
print(c1.wheels)

c2 = Car()
c2.model = 'porsche'
breakpoint()

#c1.log_me()
#Car.wheels = 7
#c1.log_me()
#
#c2 = Car()
#c2.model = 'porsche'
#c2.log_me()
