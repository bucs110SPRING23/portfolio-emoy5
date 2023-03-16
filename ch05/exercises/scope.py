def multiplication(x, y):
    result = 0
    for i in range(y):
        result = x + x
    return result
    
def exponents(s, t):
    result = 1
    for i in range(t):
        result = result * s
    return result

def square(z):
    result = exponents(z,2)
    return result

def main():
    print(multiplication(3, 4))
    print(exponents(2, 3))
    print(square(4))
main()