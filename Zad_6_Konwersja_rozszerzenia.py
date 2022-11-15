#!/bin/env python3
import argparse
import os

if __name__ == "__main__":
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to *.jpg file that needs extension change")
    args = parser.parse_args()

    # Checking if element given in 'path' argument is a file
    assert os.path.isfile(args.path), "Element given in 'path' argument is not a file"
    
    # Splitting given path
    localisation, filename = os.path.split(args.path)

    # File extensnion check
    assert filename.endswith(".jpg"), "Element given in 'path' argument is not a *.jpg file"

    # Extension change
    filename = filename.replace(".jpg", ".png")

    # File rename
    new_path = os.path.join(localisation, filename)
    os.rename(args.path, new_path)

