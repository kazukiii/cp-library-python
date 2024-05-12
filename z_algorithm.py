def z_algorithm(s):
    n = len(s)
    Z = [0] * n
    Z[0] = n
    left, right = -1, -1

    for i in range(1, n):
        same = 0
        if left != -1:
            same = min(Z[i - left], right - i)
            same = max(0, same)

        while i + same < n and s[same] == s[i + same]:
            same += 1

        Z[i] = same

        # update left and right
        if i + same > right:
            left = i
            right = i + same

    return Z


if __name__ == "__main__":
    # usage
    input_string = "abacaba"
    z_values = z_algorithm(input_string)
    print(z_values)  # [7, 0, 1, 0, 3, 0, 1]
