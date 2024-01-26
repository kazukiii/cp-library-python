class CumulativeSum2D:
    def __init__(self, data):
        """
        Calculate the cumulative sum of a 2D list 'data'.
        """
        h, w = len(data), len(data[0])
        self.cum = [[0] * (w + 1) for _ in range(h + 1)]

        for y in range(h):
            for x in range(w):
                self.cum[y + 1][x + 1] = (
                    data[y][x]
                    + self.cum[y + 1][x]
                    + self.cum[y][x + 1]
                    - self.cum[y][x]
                )

    def query(self, x1, y1, x2, y2):
        """
        Calculate the sum of elements in the rectangle specified by [x1, y1) to [x2, y2).
        """
        return self.cum[y2][x2] - self.cum[y1][x2] - self.cum[y2][x1] + self.cum[y1][x1]


if __name__ == "__main__":
    data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    cumsum2d = CumulativeSum2D(data)

    # Calculate the sum of elements in the range from [1, 1) to [3, 3)
    print(cumsum2d.query(1, 1, 3, 3))  # Output: 34
