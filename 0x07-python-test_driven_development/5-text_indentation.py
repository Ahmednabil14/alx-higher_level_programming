#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each\
          of these characters: ., ? and :
    argument:
        text: the original text
    exceptions:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    syntaxx = ""
    for i in range(len(text)):
        if text[i] == " " and (text[i-1] == ":" or text[i-1] == "?"
                               or text[i-1] == "."):
            continue
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            syntaxx += text[i] + "\n" + "\n"
        else:
            syntaxx += text[i]
    print(syntaxx, end='')
