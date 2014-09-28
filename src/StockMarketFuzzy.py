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
            self.stock[line[0]] = Stock(line[0], float(line[1]), float(line[2]), \
                    float(line[3]), float(line[4]), float(line[5]))
            self.dates.append(line[0])

    def __moving_average(self, init, end):
        sum = 0;
        for i in range(init, end):
            sum += self.stock[self.dates[i]].open;
        return sum / (end - init);

    def show_moving_average(self):
        mm_10_init = 40
        mm_10_end  = mm_10_init + 10
        mm_50_init = 0
        mm_50_end  = mm_50_init + 50
        day = 51
        print "Dia Real Mm_10 Mm_50"
        for i in range(0, 50):
            sum10 = self.__moving_average(mm_10_init + i, mm_10_end + i)
            sum50 = self.__moving_average(mm_50_init + i, mm_50_end + i)
            real  = self.stock[self.dates[day - 1]].open
            print "%d %.2f %.2f %.2f" % (day, real, sum10, sum50)
            day += 1


    def fuzzy(self, fuzzy_file):
        import fuzzy.storage.fcl.Reader
        system = fuzzy.storage.fcl.Reader.Reader().load_from_file(fuzzy_file);
        my_input = {"Mm_10": 1.5,#self.__moving_average(90, 100),
                    "Mm_50": 2,#self.__moving_average(50, 100),
                    "Noticia": 0}
        my_output = {"Saida": 0.0}
        system.calculate(my_input, my_output);
        print my_output["Saida"]
        #sum10 = self.__moving_average(40, 50);
        #sum50 = self.__moving_average(0, 50);
        #print sum10;
        #print sum50;
        #print self.stock[self.dates[50]].open;


if __name__ == '__main__':
    smf = StockMarketFuzzy();
    if (len(argv) > 2):
        smf.read_file(argv[1]);
        #smf.show_moving_average();
        #smf.fuzzy(argv[2]);
