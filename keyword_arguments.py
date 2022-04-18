
def simple(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    return a + b + c

print(simple(b=1, c=7, a=78))
# Referencing a keyword that doesn’t match any of the declared parameters
# generates an exception
print(simple(b=1, d=7, a=78))
