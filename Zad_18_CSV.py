#!/bin/env python3
import argparse
import csv
import os

class Movie:
    def __init__(self, id: int, title: str, year: int, rate: int) -> None:
        # Simple input validation
        # Limitations in values of propertie set to ensure propper table formatting
        assert 0 < id and id < 1000000, "Invalid index"
        assert len(title) <= 21, "Title too long"
        assert 0 < year and year < 10000, "Invalid year given"
        assert rate in range(11), "Invalid rate given"

        # Properties init
        self.id = id        # Movie ID in database
        self.title = title  # Movie title   
        self.year = year    # Rear of release
        self.rate = rate    # Movie rate from 0 to 10

    def table_row(self):
        # Method will return propertly formatted table row
        return f"| {self.id:6} | {self.title:21} | {self.year:4} |  {self.rate:2}/10 |"

    def to_dict(self):
        # Method returns dict that can be directly given to csv.DictWriter object
        return {"Title": self.title, "Year": self.year, "Rate": self.rate}


class Database:
    def __init__(self, file: str) -> None:
        # Poperties init
        self.csv_header = ["Title", "Year", "Rate"]
        self.file = file
        self.movies = list()
        self.next_id = 1

    def display(self):
        print("|--------|-----------------------|------|--------|")
        print("|   ID   |         Title         | Year |  Rate  |")
        print("|--------|-----------------------|------|--------|")

        for movie in self.movies:
            print(movie.table_row())

        print("|--------|-----------------------|------|--------|")

    def add(self, new_movie: Movie) -> bool:
        # Limitations for propper table formatting
        if self.next_id == 1000000:
            return False    # Not able to add new element
        
        # ID assigning
        new_movie.id = self.next_id
        self.next_id += 1

        # Appending self.movies list
        self.movies.append(new_movie)

        return True

    def remove(self, id_to_remove : int) -> bool:
        # Searching for given ID in database
        index_to_remove = None

        for index, movie in enumerate(self.movies):
            if movie.id == id_to_remove:
                index_to_remove = index
                break
        
        # If movie with given ID was found it will be removed
        if index_to_remove is not None:
            self.movies.pop(index_to_remove)

            # Returning True as exit status
            return True
        
        # if not False will be returned
        return False

    def read_from_file(self) -> bool:
        # Checking if given file exists
        if os.path.exists(self.file) and os.path.isfile(self.file) and self.file.endswith(".csv"):
            # Reading file content and saving it to self.movies
            with open(self.file) as file:
                csv_reader = csv.DictReader(file)

                # Iterating through rows
                for row in csv_reader:
                    # Ectracitng values
                    title = row["Title"]
                    year = row["Year"]
                    rate = row["Rate"]

                    # Adding movie to database
                    try:
                        assert self.add(Movie(1, title, int(year), int(rate))), "Too many movies in given file"   # ID does not matter here - it will be propertly set in self.add method
                    except ValueError:
                        return False    # If conversion between str and int variables fails False will be returned

            # Returnig True as indicator that data was successfully read from file
            return True
        # Returning False as indicator that given file does not exists and new database file must be created
        return False

    def write_to_file(self) -> bool:
        # Checking if given file localisation exists
        file_basename = os.path.dirname(self.file)

        if file_basename:   # If file is not placed in CWD
            if os.path.exists(file_basename):
                # Returning False as indicator that method is unable to save database to file
                return False

        # Checking file extension
        if not self.file.endswith(".csv"):
            return False

        # Opening given file
        with open(self.file, "w") as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.csv_header)
            csv_writer.writeheader()    # Adding header to the file

            # Saving movies one by one
            for movie in self.movies:
                csv_writer.writerow(movie.to_dict())

        # Returning True as success indicator
        return True
            

# Main part of the program
if __name__ == "__main__":
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("database", help="Path to *.csv file that contains movies database. If does not exist new database file will be created.")
    args = parser.parse_args()
    
    # Creating Database object
    database = Database(args.database)

    # Loading data from given file to created database
    if database.read_from_file():
        print("Content of given database:")
        database.display()
    else:
        print("Not able to read given file - new one will be created")

    # Menu
    try:
        while True:
            # Option menu
            print("Choose option: ")
            print("  0 - Display")
            print("  1 - Add")
            print("  2 - Remove")
            print("  3 - Save and quit")

            # Validationg given option
            try:
                choosen_option = int(input(">>"))
            except ValueError:
                print("Invalid option")

            if choosen_option not in range(4):
                print("Invalid option")
                continue
            
            # Options handling
            if choosen_option == 0:
                # Printing currnet content of database in form of table
                print("Database content")
                database.display()
                
            elif choosen_option == 1:
                # Adding new movie to database
                print("Adding option chosen")

                # User input
                title = input("Title (21 characters max): ")
                year = input("Year of release: ")
                rate = input("Rate from 1 to 10: ")

                # Adding new movie to database + input validation
                try:
                    new_movie = Movie(1, title, int(year), int(rate))
                    
                    if database.add(new_movie):
                        print("Operation successfull")
                    else:
                        print("Unable to add new movie to database")
                        print("Too many movies already archived in given file")

                except (AssertionError, ValueError):    # Exceptions rised in __init__ of Movie class and conversion to int
                    print("Invalid input")


            elif choosen_option == 2:
                print("Remove option chosen")
                
                # User input
                id_to_remove = input("Move ID to remove: ")

                # Removing movie from database + input validation
                try:
                    if database.remove(int(id_to_remove)):
                        print("Removing successfull")
                    else:
                        print("Not able to remove movie with given ID")
                except ValueError:  # Exception raised by conversion to int
                    print("Invalid input")

            elif choosen_option == 3:
                break   # Leaving the while loop
    finally:
        # At the end program will be trying to save database to file no matter what happened earlier
        if database.write_to_file():
            print("Database successfully saved to file")
        else:
            print("Not able to save database to file - changes lost")
            print(f"Check value of posisional argument 'database' (given value = '{args.database}')")