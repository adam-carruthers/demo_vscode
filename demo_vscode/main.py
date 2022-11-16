import pandas as pd
from .example_file import fake_input


def calc_full_name():
    """
    This function asks the user their first name and last name to get their full name
    """
    first_name = fake_input("First Name: ")
    last_name = fake_input("Surname ")

    return combine_names(first_name, last_name)


def combine_names(first_name, last_name):
    return first_name + last_name


def do_pandas_stuff_for_demo():
    titanic = pd.read_csv("titanic.csv")

    print(titanic.groupby(["Sex", "Survived"]).size())


def main():
    print("Hello and welcome to my spectacular program")

    full_name = calc_full_name()

    print(f"Your name is {full_name}")

    do_pandas_stuff_for_demo()


# Only run main() if I run this file directly
# Don't run it if this file is imported from elsewhere
if __name__ == "__main__":
    main()
