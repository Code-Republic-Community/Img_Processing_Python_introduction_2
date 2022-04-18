class Car:
    ...

class BMW(Car):
    ...

class Audi(Car):
    ...

c = Car()
b = BMW()
a = Audi()
print(isinstance(a, Car))
print(isinstance(a, Audi))
print(isinstance(c, Audi))
