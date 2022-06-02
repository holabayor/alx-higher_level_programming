#!/usr/bin/python3
import sys
import hidden_4


def main():
    file = dir(hidden_4)
    for line in file:
        if line[:2] != '__':
            print(line)


if __name__ == "__main__":
    main()
