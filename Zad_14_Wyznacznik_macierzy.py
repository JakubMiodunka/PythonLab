#!/bin/env python3
import numpy as np

if __name__ == "__main__":
    array_size = (8, 8)
    max_value = 10

    array = np.random.randint(max_value, size=array_size)

    determinant = np.linalg.det(array)

    print("Array:")
    print(array)

    print(f"Array determinant = {determinant}")

