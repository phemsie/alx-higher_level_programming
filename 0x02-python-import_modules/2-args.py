#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    print("{:d} {:s}{:s}".format(ac, 'argument' if ac == 1 else 'arguments',
        '.' if ac == 0 else ':'))
    for i in range(1, ac + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
