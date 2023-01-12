import math

def reverse(x):
    num_digits = math.floor(math.log10(x)) + 1
    x = str(x)
    for i in range(num_digits // 2):
        j = num_digits - i -1
        x[i],x[j] = x[j], x[i]
    return x


print(reverse(12456))