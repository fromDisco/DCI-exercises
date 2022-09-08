import sys
import getopt

number = input("Please")
print(number)


def get_start_and_end_dates():
    start_date = None
    end_date = None
    argv = sys.argv[1:]

    print("argv:")
    print(argv)

    print("RAW:")
    print(getopt.getopt(argv, "e:s:"))
    opts, args = getopt.getopt(
        argv, "s:e:", ["start_date=", "end_date="])

    print("opts")
    print(opts)
    print("args")
    print(args)


# get_start_and_end_dates()

import sys
print(sys.argv)