def foo(a, b):
    return a + b, a* b

print(type(foo(3, 4)))
s, m = foo(2, 3)
print(s)
print(m)
