#!/usr/bin/python3
safe_print = __import__('1-safe_print_integer').safe_print_integer
value  = 89
nb = safe_print(value)
if not nb:
    print("{} is not an integer".format(value))
value  = -89
nb = safe_print(value)
if not nb:
    print("{} is not an integer".format(value))
value  = "School"
nb = safe_print(value)
if not nb:
    print("{} is not an integer".format(value))
