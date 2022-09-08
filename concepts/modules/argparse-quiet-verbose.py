import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--quiet',
                    action='store_true',
                    dest='quiet',
                    help='Suppress Output'
                    )
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Verbose Output'
                    )
args = parser.parse_args()
print(args)

print('Quiet mode is %r.' % args.quiet)