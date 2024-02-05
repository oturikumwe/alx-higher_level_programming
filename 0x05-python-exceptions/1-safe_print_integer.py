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

# Test the function
print(safe_print_integer(42))  # Should print True
print(safe_print_integer("hello"))  # Should print False
