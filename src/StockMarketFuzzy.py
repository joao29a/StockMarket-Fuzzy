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
        self.dates = []

    def read_file(self, filename='data'):
        f = open(filename, 'r');
        for i in range(0, 2): f.readline(); #read two lines and discard them
        for line in f:
            line = line.replace('\n', '');
            line = line.split();
            self.stock[line[0]] = Stock(line[0], float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]))
            self.dates.append(line[0])

    def __moving_average(self, init, end):
        sum = 0;
        for i in range(init, end):
            sum += self.stock[self.dates[i]].open;
        return sum / (end - init);


    def fuzzy(self, fuzzy_file):
        import fuzzy.storage.fcl.Reader
        #system = fuzzy.storage.fcl.Reader.Reader().load_from_file(fuzzy_file);
        sum10 = self.__moving_average(40, 50);
        sum50 = self.__moving_average(0, 50);
        print sum10;
        print sum50;
        print self.stock[self.dates[50]].open;


if __name__ == '__main__':
    smf = StockMarketFuzzy();
    if (len(argv) > 2):
        smf.read_file(argv[1]);
        smf.fuzzy(argv[2]);
