#!/bin/env python3

if __name__ == "__main__":
    # Setting code
    CODE = "1234"

    # User input
    user_input = input("Enter code: ")

    # Comparing user input to code
    if user_input == CODE:
        print("Access granted")
    else:
        print("Access denyed")