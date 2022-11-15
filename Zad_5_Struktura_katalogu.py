#!/bin/env python3

import os


if __name__ == "__main__":
    # Setting up path where alaysis should start
    BEGIN_PATH = "/home/jm"

    # 'Walking' through path given above 
    for dirpath, *_, filenames in os.walk(BEGIN_PATH):
        # Printing all files in current location
        print(f"Current location: {dirpath}  Files: {', '.join(filenames)}")