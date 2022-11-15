#!/bin/env python3
import random


def bubble_sort(to_sort: list) -> list:
    # Making a copy of given list
    copy = to_sort.copy()

    # Executong bubble sort algorythm
    size = len(copy)
    for _ in copy:
        for index, _ in enumerate(copy):
            if index < size - 1:
                if copy[index] > copy[index + 1]:
                    temp = copy[index]
                    copy[index] = copy[index + 1]
                    copy[index + 1] = temp
    # Returning sorted list
    return copy


if __name__ == "__main__":
    # Random numbers generation
    numbers = list()
    for _ in range(50):
        numbers.append(random.uniform(0, 101))  #floats in range <0; 100>

    # Sorting of generated list
    sorted = bubble_sort(numbers)

    # Printing results
    print(f"Genrrated numbers: {numbers}")
    print(f"Sorted: {numbers}")

    # Additional check of implemented algorythm
    numbers.sort()
    assert numbers == sorted, "Implemented algorythom not valid"

