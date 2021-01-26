
import re


def split_by_regular_expression(text, splitter):
    """
    Splits text using splitter pattern or 're' compiled object
    """

    if type(splitter) == str:

        return re.split(splitter, text)
    
    return splitter.split(text)


class RE_patterns:

    spaces = re.compile(r"[\s]+")

