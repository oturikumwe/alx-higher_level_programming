#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e)
        return False
