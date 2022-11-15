#!/bin/env python3
import argparse
from cmath import sqrt

if __name__ == "__main__":
    # Parsing elements of ax^2 + bx + c function to the script as separate arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("c", type=int)
    args = parser.parse_args()

    # Computing delta value
    delta = args.b**2 - 4 * args.a * args.c

    # List where equation will be stored
    roots = list()

    # Computing roots of the equation
    if delta == 0:
        root = ((-1) * args.b - sqrt(delta))/(2 * args.a)
        roots.append(root)
    elif delta > 0:
        root_A = ((-1) * args.b - sqrt(delta))/(2 * args.a)
        root_B = ((-1) * args.b + sqrt(delta))/(2 * args.a)

        roots.append(root_A)
        roots.append(root_B)

    # Printing output
    print(f"{len(roots)} roots exists:")
    for root in roots:
        print(root)


