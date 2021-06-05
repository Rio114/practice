import sys
import pdb


def log(args):
    print(args)


def calc(a, b):
    return a + b


def main(args):
    a = 3
    b = 2
    log(args)
    pdb.set_trace()
    c = calc(a, b)
    log(c)


if __name__ == "__main__":
    main(sys.argv)
