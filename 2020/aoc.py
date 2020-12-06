def lines(path):
    """
    Return a list of lines from the file `path`
    """
    with open(path) as f:
        return f.readlines()


def file(path):
    """
    Return contents of a file at `path` as a string
    """
    with open(path) as f:
        return f.read()


def filerstrip(path):
    """
    Return rstripped file contents of file at `path`
    """
    return file(path).rstrip()


def load_map(path):
    """
    Return list of strings ("2D array") from the file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: x.rstrip(), lines))


def load_ints(path):
    """
    Return a list of ints loaded from file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: int(x.rstrip()), lines))
