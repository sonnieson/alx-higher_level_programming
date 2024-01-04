#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # The first element in sys.argv is the script name
    if argc == 0:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
