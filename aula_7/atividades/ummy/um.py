import re
import sys


def main():
    print(count(input("Text: ")))


def count(uhum):
    um = r'(?<![\w])um(?![\w])'
    finder = re.findall(um, uhum)
    counter =len(finder)
    return counter


if __name__ == "__main__":
    main()