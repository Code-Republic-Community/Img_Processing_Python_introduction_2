def printer(func):
    def wrapper(*arg, **kwargs):
        print('Starting')
        func(*arg, **kwargs)
        print('End')

    return wrapper

@printer
def greeting(a):
    print(f'Good Morning from {a}')

@printer
def greeting_2(a, b):
    print(f'Good Bye from {a} {b}')

greeting('Singapore')
greeting_2('Singapore', 'Armenia')
