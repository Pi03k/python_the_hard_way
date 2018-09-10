#!/usr/bin/env python3

from sys import argv

script, filename = argv


def eraseFile(filename):
    print("Erasing file")
    file = open(filename, 'w')
    file.truncate()
    file.close()


print(f"We are going to erase {filename}")
print(f"Contents of {filename}")
print(open(filename).read())
answer = input('[Y/n] ')

if answer == 'Y':
    eraseFile(filename)
