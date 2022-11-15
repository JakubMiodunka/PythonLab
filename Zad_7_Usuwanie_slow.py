#!/bin/env python3
import argparse


if __name__ == "__main__":
    # Parsing text as script argument
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()

    # List where words that should be removed are stored
    TO_REMOVE = ("się", "i", "oraz", "nigdy", "dlaczego")

    # Splitting given text to list
    words = args.text.split()

    # Words removal
    for index, word in enumerate(words):
        if word in TO_REMOVE:
            words.pop(index)

    # Joining text together
    print(" ".join(words))
