#!/bin/env python3

if __name__ == "__main__":
    # User input
    user_input = input("Type Your name, surname and year of birth: ").split()
    
    # Basic input validation
    assert len(user_input) == 3, "Input format not valid"

    # Variables unpacking
    name, surname, year_of_birth = user_input
    
    # Printing result
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Year of birth: {year_of_birth}")