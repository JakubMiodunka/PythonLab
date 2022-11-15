#!/bin/env python3

if __name__ == "__main__":
    vector_A = [1, 2, 3, 4, 5]
    vector_B = [2, 3, 4, 5, 6]

    assert len(vector_A) == len(vector_B), "Vectors not the same length"

    result = 0
    for a, b in zip(vector_A, vector_B):
        result += a * b

    print(f"Vector A: {vector_A}")
    print(f"Vector B: {vector_B}")
    print(f"Result: {result}")

