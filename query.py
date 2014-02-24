#!/usr/bin/env python

from ystockquote import (
    get_all,
    get_historical_prices
)


def parse_args():
  import argparse
  parser = argparse.ArgumentParser(
      description='YStockQuote: historical or detailed live quotes. To get historical quotes, provide a start end end date, else it will give a live quote.')
  parser.add_argument('-s', '--symbol')
  parser.add_argument('-sd', '--startDate', help='YYYY-mm-dd')
  parser.add_argument('-ed', '--endDate', help='YYYY-mm-dd')
  args = parser.parse_args()
  return args


def main():
  args = parse_args()
  if args.startDate and args.endDate:
    values = get_historical_prices(
        args.symbol, args.startDate, args.endDate).items()
  else:
    values = get_all(args.symbol).items()
  for val in sorted(values):
    print val


if __name__ == "__main__":
  main()

