def multiplication(x, y):
    result = 0
    for i in range(y):
        """
        multiplies two numbers without using "*"
        args: x (int), y (int)
        returns: (int)
        """
        result = result + x
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
    print(multiplication(1, 4))
    print(exponents(2, 5))
    print(square(12))
main()