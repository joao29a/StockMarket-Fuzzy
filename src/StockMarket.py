#!/usr/bin/python

from sys import argv
import Quandl

def get_market_value(stock='all'):
    filename = 'WIKI_tickers.csv'
    if (stock == 'all'):
        f = open(filename, 'r')
        f.readline()
        for line in f:
            stock_value = line.replace('"','').replace('\n','').split(',', 1)
            print "%-10s : %s" % (stock_value[0], stock_value[1])
            #print Quandl.get(stock_value[0])
    else:
        print Quandl.get(stock)


if __name__ == '__main__':
    if (len(argv) == 1):
        get_market_value()
    elif (len(argv) > 1):
        get_market_value(argv[1])
