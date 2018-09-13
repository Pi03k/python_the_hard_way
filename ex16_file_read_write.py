#!/usr/bin/env python3

from sys import argv


def eraseFile(filename):
    print("Erasing file")
    file = open(filename, 'w')
    file.truncate()
    file.close()


def main(filename):
    print(f"We are going to erase {filename}")
    print(f"Contents of {filename}")
    print(open(filename).read())
    answer = input('[Y/n] ')

    if answer == 'Y':
        eraseFile(filename)


if __name__ == "__main__":
    filename = argv[1]
    main(filename)
