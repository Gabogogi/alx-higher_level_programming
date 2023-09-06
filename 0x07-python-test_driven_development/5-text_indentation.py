#!/usr/bin/python3

"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    while flag < len(text) and text[flag] == ' ':
        flag += 1

    while flag < len(text):
        print(text[flag], end="")
        if text[flag] == "\n" or text[flag] in ".?:":
            if text[flag] in ".?:":
                print("\n")
            flag += 1
            while flag < len(text) and text[flag] == ' ':
                flag += 1
            continue
        flag += 1
