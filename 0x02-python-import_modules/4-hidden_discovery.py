#!/usr/bin/python3
import hidden_4


def main():
    file = dir(hidden_4)
    length = len(file)
    for i in range(length):
        if file[i][:2] != '__':
            print(file[i])


if __name__ == "__main__":
    main()
