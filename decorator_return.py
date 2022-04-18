def printer(func):
    def wrapper(*arg, **kwargs):
        print('Starting')
        ret = func(*arg, **kwargs)
        print('End')
        return ret

    return wrapper

@printer
def add(a, b):
    return a + b


print(add(1, 2))
