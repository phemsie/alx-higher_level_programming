#!/usr/bin/python3
""" a module for text indentaion method """


def text_indentation(text):
    """ function to that prints a text with 2 new
    lines after each of these characters: ., ? and :
    Args:
        text: type str text to be processed
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
