#!/usr/bin/python3
"""
This module contains script to work with the command line.
"""


def validate_bold(line):
    """
    Validate if the line has bold or italic text.
    """
    index = line.find("**")
    res_str = ""

    if index != -1:
        res_str += line[:index] + "<b>"
        new_str = line[index + 2:]
        idx = new_str.find("**")
        if idx != -1:
            if idx + 1 == len(new_str):
                result += new_str[:idx] + "</b>\n"
            else:
                res_str += new_str[:idx] + "</b>"
                res_str += validate_bold(new_str[idx + 2:])
