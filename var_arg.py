def average(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

# Tuple packing
avg = average(1, 2, 3, 4)
print(avg)
