#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("This is a type exception")
    except TypeError as e:
        print("Exception:", e)
