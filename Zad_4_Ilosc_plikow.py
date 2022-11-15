#!/bin/env python3

import os


if __name__ == "__main__":
    # Setting path to check
    PATH = "/dev"

    # Creating file counter
    file_counter = 0

    # Checking recursively given path in search for files
    for *_, filenames in os.walk(PATH):
        # Updating file counter
        file_counter += len(filenames)

    # Printing result
    print(f"Number of files in {PATH}: {file_counter}")