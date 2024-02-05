#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()  # Add a newline after printing the integer
        return True
    except (TypeError, ValueError):
        return False
