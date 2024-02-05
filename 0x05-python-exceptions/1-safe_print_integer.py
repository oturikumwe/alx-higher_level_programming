#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()  # Add a newline after printing the integer
        return True
    except(TypeError, ValueError):
        return False


# Test the function
print(safe_print_integer(42))  # Should print True
print(safe_print_integer("hello"))  # Should print False
