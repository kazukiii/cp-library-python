def prime_factorize(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    factor = 3
    while factor * factor <= number:
        if number % factor == 0:
            factors.append(factor)
            number //= factor
        else:
            factor += 2

    if number != 1:
        factors.append(number)

    return factors


if __name__ == "__main__":
    result = prime_factorize(60)
    print(result)  # [2, 2, 3, 5]
