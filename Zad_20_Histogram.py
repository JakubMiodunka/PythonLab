#!/bin/env python3
import multiprocessing
import time
import random


def task(data: list):
    result = dict()
    for element in data:
        result[element] = result.get(element, 0) + 1

    return result


if __name__ == '__main__':
    # Picking up size of input data
    size = 2000

    # Logging
    print(f"Size: {size}")

    # Creating matrix with dim <size> x <size>
    data = list()
    for _ in range(size):
        row = list()
        for _ in range(size):
            row.append(random.randint(0, 10))
        data.append(row)

    # Multi core processing
    print("Multi core processing start")
    cpu_quantity = multiprocessing.cpu_count()
    with multiprocessing.Pool(cpu_quantity) as pool:
        start_time = time.perf_counter()
        result = [pool.apply_async(task, args=(row,1)) for row in data]
        end_time = time.perf_counter()
    print(f"Multi core processing time: {end_time - start_time}")

    # Single core processing
    print("Single core processing start")
    start_time = time.perf_counter()
    result = [task(row) for row in data]
    end_time = time.perf_counter()
    print(f"Single core processing time: {end_time - start_time}")

    """
    Console output for size 2000:
        Size: 2000
        Multi core processing start
        Multi core processing time: 0.01618253700007699
        Single core processing start
        Single core processing time: 0.3418869980000636
    """

