#!/usr/bin/env python3

import sys


def main(language_file, encoding, errors):
    line = language_file.readline()
    while line:
        print_line(line, encoding, errors)
        line = language_file.readline()


def print_line(line, encoding, errors):
    nextLang = line.strip()
    rawBytes = nextLang.encode(encoding, errors=errors)
    cookedString = rawBytes.decode(encoding, errors=errors)
    print(rawBytes, "<==>", cookedString)


if __name__ == "__main__":
    script, inputFile, inputEncoding, error = sys.argv
    languages = open(inputFile, encoding='utf-8')
    main(languages, inputEncoding, error)
