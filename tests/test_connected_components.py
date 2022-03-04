import numpy as np
import unittest

from connected_components import connected_components


class TestConnectedComponents(unittest.TestCase):
    def test_case0(self):
        A0 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        r0 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(connected_components(A0).tolist(), r0.tolist())

    def test_case1(self):
        A1 = np.array([[1, 1, 0], [0, 0, 1], [1, 0, 0]])
        r1 = np.array([[1, 1, 0], [0, 0, 1], [2, 0, 0]])
        self.assertEqual(connected_components(A1).tolist(), r1.tolist())

    def test_case2(self):
        A2 = np.array([[2, 4, 5, 6], [7, 8, 9, 10], [2, 3, 4, 5]])
        r2 = np.zeros_like(A2)
        self.assertEqual(connected_components(A2).tolist(), r2.tolist())

    def test_case3(self):
        A3 = np.array([[1, 1, 0, 1, 0, 1, 1, 1, 0]])
        r3 = np.array([[1, 1, 0, 2, 0, 3, 3, 3, 0]])
        self.assertEqual(connected_components(A3).tolist(), r3.tolist())

    def test_empty(self):
        A_empty = np.array([[]])
        r_empty = np.zeros_like(A_empty)
        self.assertEqual(connected_components(A_empty).tolist(), r_empty.tolist())


if __name__ == '__main__':
    unittest.main()