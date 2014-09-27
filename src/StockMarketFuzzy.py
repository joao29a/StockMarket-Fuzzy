#!/usr/bin/python

from sys import argv

class Stock:
    def __init__(self, date, open, high, low, close, volume):
        self.date = date;
        self.open = open;
        self.high = high;
        self.low = low;
        self.close = close;
        self.volume = volume;

class StockMarketFuzzy:
    def __init__(self):
        self.stock = {}

    def read_file(self, filename='data'):
        f = open(filename, 'r');
        for i in range(0, 2): f.readline(); #read two lines and discard them
        for line in f:
            line = line.replace('\n', '');
            line = line.split();
            self.stock[line[0]] = Stock(line[0], line[1], line[2], line[3], line[4], line[5])

    def fuzzy(self, fuzzy_file):
        import fuzzy.storage.fcl.Reader
        system = fuzzy.storage.fcl.Reader.Reader().load_from_file(fuzzy_file);

if __name__ == '__main__':
    smf = StockMarketFuzzy();
    if (len(argv) > 2):
        smf.read_file(argv[1]);
        smf.fuzzy(argv[2]);
