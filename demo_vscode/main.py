print("hello")

def calc_full_name():
    """
    This function asks the user their first name and last name to get their full name
    """
    first_name = input("What's your first name? ")
    last_name = input("What's your surname? ")

    return first_name + last_name

full_name = calc_full_name()

print(f"Your name is {full_name}")
