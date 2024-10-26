import unittest

from data_structures_and_algorithms.algorithms.fibonacci import fibonacci_top_down, fibonacci_bottom_up, \
    fibonacci_recursive


class Test(unittest.TestCase):
    def setUp(self):
        self.n = 6  # iterations

    def test_fibonacci_recursive(self):
        results = []

        for i in range(self.n + 1):
            results.append(fibonacci_recursive.fibonacci(i))

        self.assertTrue(self._check(results))

    def test_fibonacci_top_down(self):
        results = []

        for i in range(self.n + 1):
            results.append(fibonacci_top_down.fibonacci(i))

        self.assertTrue(self._check(results))

    def test_fibonacci_bottom_up(self):
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


if __name__ == '__main__':
    unittest.main()
