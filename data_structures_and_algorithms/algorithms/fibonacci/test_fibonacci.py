import unittest

from data_structures_and_algorithms.algorithms.fibonacci import (
    fibonacci_bottom_up,
    fibonacci_recursive,
    fibonacci_top_down,
)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.n = 6  # iterations

    def test_fibonacci_recursive(self) -> None:
        results = []

        for i in range(self.n + 1):
            results.append(fibonacci_recursive.fibonacci(i))

        self.assertTrue(self._check(results))

    def test_fibonacci_top_down(self) -> None:
        results = []

        for i in range(self.n + 1):
            results.append(fibonacci_top_down.fibonacci(i))

        self.assertTrue(self._check(results))

    def test_fibonacci_bottom_up(self) -> None:
        results = []

        for i in range(self.n + 1):
            results.append(fibonacci_bottom_up.fibonacci(i))

        self.assertTrue(self._check(results))

    def _check(self, results: list) -> bool:
        if self.n == 0:
            return len(results) == 1 and results[0] == 0

        if self.n == 1:
            return len(results) == 2 and results[0] == 0 and results[1] == 1

        nm2 = results[0]
        nm1 = results[1]

        for i in range(2, self.n):
            if results[i] != nm1 + nm2:
                return False

            nm2 = nm1
            nm1 = results[i]

        return True


if __name__ == "__main__":
    unittest.main()
