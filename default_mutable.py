#def foo(arr=[]):
#    arr.append('###')
#    return arr
#
#a = foo([])
#print(a)
#b = foo([])
#print(b)
#c = foo()
#print(c)

def foo_2(arr=None):
    if arr is None:
        arr = []
    arr.append('###')
    return arr

a = foo_2()
print(a)
b = foo_2()
print(b)
