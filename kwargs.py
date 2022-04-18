def foo(**kwargs):
    #dict packing
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
       print(key, '->', val)


foo(count=2, fruite'banana', price = 600)
