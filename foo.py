def foo(count, fruit, price):
    print('Called')
    return fruit + " fruit ", count * price, "its me"


print(type(foo(count=7, price=0.5, fruit='apple')))
a  = foo(count=7, price=0.5, fruit='apple')
#print(a)
#print(b)
#a = foo(count=7, price=0.5, fruit='apple')
#print(a['fruit'])
#print(a['total'])
