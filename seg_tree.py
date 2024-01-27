import typing


class SegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    @staticmethod
    def _ceil_pow2(n: int) -> int:
        x = 0
        while (1 << x) < n:
            x += 1

        return x


if __name__ == "__main__":
    # Define the operation for the segment tree.
    # In this case, it's a sum operation.
    def op(x, y):
        return x + y

    # Define the identity element for the sum operation.
    # For sum, the identity element is 0, because adding 0 to any number doesn't change the number.
    e = 0

    # Create an array of numbers.
    array = [1, 2, 3, 4, 5]

    # Create the segment tree with the defined operation, identity element, and the array.
    seg_tree = SegTree(op, e, array)

    # Get the sum of elements from index 1 to 3 (inclusive).
    print("Sum of elements from index 1 to 3:", seg_tree.prod(1, 4))

    # Update the element at index 2 to 10. -> [1, 2, 10, 4, 5]
    seg_tree.set(2, 10)

    # After the update, get the sum of elements again from index 1 to 3 (inclusive).
    print("Sum after update:", seg_tree.prod(1, 4))

    # Get the product of all elements in the array.
    print("Product of all elements:", seg_tree.all_prod())

    # Find the maximum right index for which the sum of elements from index 1 to that index (not inclusive) is less than or equal to 12.
    def f(x):
        return x <= 12

    print("Maximum right index:", seg_tree.max_right(1, f))

    # Find the minimum left index for which the sum of elements from that index to index 3 (not inclusive) is less than or equal to 12.
    print("Minimum left index:", seg_tree.min_left(3, f))
