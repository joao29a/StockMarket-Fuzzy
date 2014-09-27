#!/usr/bin/python

from sys import argv
import Quandl

def get_market_value(stock='all', start='', end='', size=0):
    filename = 'WIKI_tickers.csv'
    if (stock == 'all'):
        f = open(filename, 'r')
        f.readline()
        for line in f:
            stock_value = line.replace('"','').replace('\n','').split(',', 1)
            print "%-10s : %s" % (stock_value[0], stock_value[1])
    else:
        data = Quandl.get(stock, trim_start=start, trim_end=end)
        if (size == 0): print data
        else: print data.head(size).to_string()


if __name__ == '__main__':
    if (len(argv) == 1):
        get_market_value()
    elif (len(argv) > 1):
        get_market_value(argv[1], argv[2], argv[3], int(argv[4]));
