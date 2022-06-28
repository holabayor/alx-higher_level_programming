#!/usr/bin/python3
"""Solves the N queen problem"""


import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        exit(1)
    if not isinstance(sys.argv[1], int):
        print("N must be a number\n")
        exit(1)
    if sys.argv[1] < 4:
        print("N must be atleast 4\n")
        exit(1)
