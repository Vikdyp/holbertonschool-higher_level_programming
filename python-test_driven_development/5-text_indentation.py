#!/usr/bin/python3
"""Module that provide a function that print a text"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of these
     characters: . ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    result = ""

    for i in text:
        result += i
        if i in separators:
            print(result.strip())
            print()
            result = ""
    if result.strip():
        print(result.strip(), end="")
