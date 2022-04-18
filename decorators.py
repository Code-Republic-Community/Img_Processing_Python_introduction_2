def printer(func):
    def wrapper():
        print('Starting')
        func()
        print('End')

    return wrapper

#def greeting():
#    print('Good Morning')
#
#
#print(greeting)
#
#print(printer(greeting))
#
#printer(greeting)()

## Function aliasing
#greeting = printer(greeting)
#greeting()
#
@printer
def greeting_dec():
    print('Good Morning')

greeting_dec()
