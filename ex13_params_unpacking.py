#!/usr/bin/env python3

from sys import argv
script, first, second, third = argv

print(f"The script is called: {script}")
print(f"Your first argument is {first}")
print(f"All arguments are: {argv}")

# Is unpacking input() possible? Doesn't look so.

argv = input("Input to assign to argv")
print(f"You've inputted {argv}")
