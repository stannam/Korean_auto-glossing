import os
import sys


def comb(list):
    """
    get a list and combine the elements with '-', except for the final symbols. e.g., ['keki', 'ta', '.'] becomes 'keki-ta'
    :param list:
    :return: str. a dash delimited string
    """
    SYMBOLS = '{}()[].!?,:;+-*/&|<>=~‘’“”\'\"'
    result = ''

    joined = '-'.join(list)

    for i, l in enumerate(joined):
        if l in SYMBOLS and joined[i-1] == '-':
            result = result[:-1]

        result += l

    return result



def csv(path, header=True):
    pattern, subs = [], []

    if hasattr(sys, "frozen"):
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        path = os.path.join(bundle_dir, 'resources', path)
    else:
        path = os.path.join(os.getcwd(), 'resources', path)

    with open(path, "r", encoding="utf-8") as f:
        if header:
            next(f)
        for line in f:
            items = line.split(",")
            pattern.append(items[0].strip())
            subs.append(items[1].strip())
    return pattern, subs
