def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    num1 = 48
    num2 = 18
    print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
