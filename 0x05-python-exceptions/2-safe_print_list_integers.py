#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
        except IndexError:
            pass
    print()  # Add a newline after printing all integers
    return printed_integers
