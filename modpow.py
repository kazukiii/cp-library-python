def modpow(a, n, m):
    if n == 0:
        return 1

    half = modpow(a, n // 2, m)
    res = (half * half) % m

    if n & 1:
        res = (res * a) % m

    return res


if __name__ == "__main__":
    result = modpow(3, 4, 5)
    print(result)  # 3^4 % 5 = 1
