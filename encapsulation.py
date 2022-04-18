class Person:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    def display(self):
        print(self.__name)
        print(self.__age)

person = Person('Areg', 30)
#accessing using class method
person.display()
#accessing directly from outside
breakpoint()
print(person.__name)
print(person.__age)

