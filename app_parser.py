import argparse


"""
Parser command in script.

Commands for script.
py main.py --days -d value [--currency -c value -> CHF,CZK,EUR,GBP,PLN,USD]
"""


parser = argparse.ArgumentParser(description='A console utility that returns '
                                             'the EUR and USD rate to PrivatBank over the past few days (1-10).'
                                             'and -currency CHF,CZK,EUR,GBP,PLN,USD')

parser.add_argument('-d', '--days', type=int, required=True)
parser.add_argument('-c', '--currency', type=str)

args = vars(parser.parse_args())  # object -> dict
days = args.get('days')
currency = args.get('currency')
