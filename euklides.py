def gcd_basic(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
a = 48
b = 18
result = gcd_basic(a, b)
print(f"GCD of {a} and {b} is {result}")


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return (gcd, y, x - (a // b) * y)

# Example usage:
a = 48
b = 18
gcd, x, y = extended_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients (x, y) are ({x}, {y})")