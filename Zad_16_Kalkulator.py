#!/bin/env python3

from Zad_15_Liczby_zespolone import Complex

def input_complex() -> Complex:
    re = float(input("    Re: "))
    im = float(input("    Im: "))

    return Complex(re, im)
    
if __name__ == "__main__":
    print("First complex (A):")
    complex_A = input_complex()

    print("Second complex (B):")
    complex_B = input_complex()

    operations = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    operation = input(f"Operation ({'/'.join(operations.values())}): ")

    assert operation in operations.values(), "Invalid operation chosen"

    if operation == operations["add"]:
        result = complex_A + complex_B
    elif operation == operations["sub"]:
        result = complex_A - complex_B
    elif operation == operations["mul"]:
        result = complex_A * complex_B
    else:   # Division
        result = complex_A / complex_B

    print(f"Result: {complex_A()} {operation} {complex_B()} = {result()}")
