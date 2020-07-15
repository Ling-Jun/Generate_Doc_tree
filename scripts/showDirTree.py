"""
pipreqs <path> generates dependency file.

pipreqs will not add Python standard library into requirements.txt,
this can be verified by running pipreqs on this folder.
"""
from pathlib import Path
import argparse
# argparse allows us to add flags such as -path to specify what each param is.
import sys


# prefix components:
space = '    '
branch = '│   '
# pointers:
tee = '├── '
last = '└── '


def tree(dir_path: Path, prefix: str = ''):
    """
    Yield a visual tree structure line by line given a directory Path object.

    colon introduces FUNCTION ANNOTATION to ensure that dir_path is a Path
    object, prefix is passed as a str object.
    https://docs.python.org/3/library/typing.html
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        # zip() returns a zip object, an iterator of tuples where the 1st item
        # in each passed iterator is paired together, then the 2nd item in each
        # passed iterator are paired together etc.
        yield prefix + pointer + path.name
        # 'yield' suspends a function’s execution and sends a value back to the
        # caller, but retains enough state to enable function to resume where
        # it is left off.
        if path.is_dir():  # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)


def parse_CLI_args():
    """Read arguments from CLI."""
    parser = argparse.ArgumentParser(description="Do something.")
    parser.add_argument("--path", "-path", default='D:/Git/GitWorkingDir/LSTM-Stock-price')
    args = parser.parse_args(sys.argv[1:])
    return args


if __name__ == '__main__':
    args = parse_CLI_args()
    # for line in tree(Path('D:\Git\GitWorkingDir')):
    # for line in tree(Path.home()):
    for line in tree(Path(args.path)):
        print(line)
