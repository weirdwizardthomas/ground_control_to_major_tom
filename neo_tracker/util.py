import itertools


def flatten_list(data):
    # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    return list(itertools.chain.from_iterable(data))