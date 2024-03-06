import random


class RollingHash:
    def __init__(self, sequence, mod=(1 << 61) - 1, base=None):
        self.mod = mod
        self.sequence = sequence
        if base is None:
            self.base = random.randint(2, mod - 2)
        else:
            self.base = base
        self.hash = [0] * (len(sequence) + 1)
        self.pow_base = [1] * (len(sequence) + 1)

        for i in range(len(sequence)):
            self.hash[i + 1] = (self.hash[i] * self.base + sequence[i]) % self.mod
            self.pow_base[i + 1] = (self.pow_base[i] * self.base) % self.mod

    def get_hash(self, left, right):
        """Returns the hash value of the subsequence from left (inclusive) to right (exclusive)."""
        return (
            self.hash[right] - self.hash[left] * self.pow_base[right - left]
        ) % self.mod


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    rh = RollingHash(sequence)
    print(rh.get_hash(0, 5) == rh.get_hash(5, 10))  # True
    print(rh.get_hash(0, 5) == rh.get_hash(0, 5))  # True
    print(rh.get_hash(0, 5) == rh.get_hash(0, 6))  # False
