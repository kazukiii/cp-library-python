class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


if __name__ == "__main__":
    # Create an instance of BIT (size is 6). Note: This implementation is 1-indexed.
    bit = Bit(6)

    # Update the sequence: Add 5 at index 2 -> [0, 5, 0, 0, 0, 0]
    # Note: Indexing starts from 1.
    bit.add(2, 5)

    # Update the sequence: Add 3 at index 5 -> [0, 5, 0, 0, 3, 0]
    bit.add(5, 3)

    # Calculate the total from index 1 to index 4
    # Note: Indexing starts from 1.
    print(bit.sum(4))  # Output: 5

    # Calculate the total from index 1 to index 6
    print(bit.sum(6))  # Output: 8
