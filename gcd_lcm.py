from fractions import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def extgcd(a, b, x, y):
    if b == 0:
        return [a, x, y]
    
    d, x, y = extgcd(b, a % b, y, x)
    y -= a // b * x
    return [d, x, y]