#!/usr/bin/python3

def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        print()  # Add a newline after printing the integer
        return True
    except (TypeError, ValueError) as e:
        print("Error:", e)
        return False
