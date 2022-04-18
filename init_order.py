class A:
    def __init__(self):
        print('from A')

class B(A):
    def __init__(self):
        super().__init__()
        print('from B')


b = B()
