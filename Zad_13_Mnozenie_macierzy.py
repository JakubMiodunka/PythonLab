#!/bin/env python3
import numpy as np

if __name__ == "__main__":
    array_size = (8, 8)
    max_value = 10

    array_A = np.random.randint(max_value, size=array_size)
    array_B = np.random.randint(max_value, size=array_size)

    result_A = np.matmul(array_A, array_B)
    result_B = np.multiply(array_A, array_B)

    print("Array A:")
    print(array_A)

    print("Array B:")
    print(array_B)

    print("Matrix product of two arrays:")
    print(result_A)

    print("Element-wise matrix multiplication of two arrays:")
    print(result_B)