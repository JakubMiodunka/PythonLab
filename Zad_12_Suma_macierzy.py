#!/bin/env python3
import numpy as np

if __name__ == "__main__":
    array_size = (128, 128)
    max_value = 10

    array_A = np.random.randint(max_value, size=array_size)
    array_B = np.random.randint(max_value, size=array_size)

    result = array_A + array_B

    print("Array A:")
    print(array_A)

    print("Array B:")
    print(array_B)

    print("Sum result array:")
    print(result)

