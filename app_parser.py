import argparse


"""
Parser command in script.

Commands for script.
py main_old.py --days -d value
"""


parser = argparse.ArgumentParser(description='A console utility that returns '
                                             'the EUR and USD rate to PrivatBank over the past few days.')
parser.add_argument('-d', '--days', type=int, required=True)
args = vars(parser.parse_args())  # object -> dict
days = args.get('days')
