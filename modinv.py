def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a, b = b, a - t * b
        u, v = v, u - t * v
    u %= m
    if u < 0:
        u += m
    return u


if __name__ == "__main__":
    for i in range(1, 13):
        print(f"{i}'s inv: {modinv(i, 13)}")
