import numpy as np
from typing import Deque
from collections import deque


def connected_components(A: np.ndarray) -> np.ndarray:
    """Breadth-first search algorithm applied for finding connected components in a grid."""

    rows, columns = A.shape

    result = np.zeros_like(A)
    component: int = 0

    Q: Deque = deque()

    for i in range(rows):
        for j in range(columns):
            if A[i][j] != 1 or result[i][j] != 0:
                continue
            component += 1
            Q.append((i, j))
            result[i][j] = component
            while Q:
                qi, qj = Q.pop()
                for ii in range(qi - 1, qi + 2):
                    for jj in range(qj - 1, qj + 2):
                        if 0 <= ii < rows and 0 <= jj < columns:
                            if result[ii][jj] != 0 or A[ii][jj] != 1:
                                continue
                            result[ii][jj] = component
                            Q.append((ii, jj))

    return result