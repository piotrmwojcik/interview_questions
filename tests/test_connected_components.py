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


if __name__ == '__main__':
    unittest.main()