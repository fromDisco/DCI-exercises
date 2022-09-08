import argparse


# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='arg1', help="please enter number")
parser.add_argument("-d", "--drag", dest='arg2', help="This is the second argument")

# Parse and print the results
args = parser.parse_args()
print(args.d)