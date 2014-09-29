#!/usr/bin/python

from StockMarketFuzzy import *
import Tkinter

class TkinterFuzzy:
    def __init__(self):
        self.tk = Tkinter.Tk();
        self.tk.title('Stock Market Fuzzy');
        self.tk.resizable(0, 0);
        self.__init_option_file();
        self.__init_entries();
        self.__init_radiobuttons();
        self.__init_button();
        self.smf = StockMarketFuzzy();

    def __init_option_file(self):
        frame = Tkinter.Frame(self.tk);
        frame.pack(anchor = Tkinter.W);
        self.option_value = Tkinter.IntVar();
        Tkinter.Checkbutton(frame, text='Usar arquivo', variable=self.option_value, \
                command=self.__set_entries).pack();

    def __set_entries(self):
        if (self.option_value.get()): self.__disable_entries();
        else: self.__enable_entries();

    def __disable_entries(self):
        self.e_mm10.configure(state = Tkinter.DISABLED);
        self.e_mm50.configure(state = Tkinter.DISABLED);

    def __enable_entries(self): 
        self.e_mm10.configure(state = Tkinter.NORMAL);
        self.e_mm50.configure(state = Tkinter.NORMAL);

    def __init_entries(self):
        frame = Tkinter.Frame(self.tk);
        frame.pack(anchor = Tkinter.W);
        Tkinter.Label(frame, text='Media movel 10 dias:').pack(side = Tkinter.LEFT);
        self.e_mm10 = Tkinter.Entry(frame, bd=5);
        self.e_mm10.pack(side = Tkinter.LEFT);
        frame = Tkinter.Frame(self.tk);
        frame.pack(anchor = Tkinter.W);
        Tkinter.Label(frame, text='Media movel 50 dias:').pack(side = Tkinter.LEFT);
        self.e_mm50 = Tkinter.Entry(frame, bd=5);
        self.e_mm50.pack(side = Tkinter.LEFT);

    def __init_radiobuttons(self):
        frame = Tkinter.Frame(self.tk);
        frame.pack(anchor = Tkinter.W);
        Tkinter.Label(frame, text='Noticia:').pack(side = Tkinter.LEFT);
        self.rb_notice = Tkinter.IntVar();
        Tkinter.Radiobutton(frame, text='Positivo', variable=self.rb_notice, \
                value=1).pack(side = Tkinter.LEFT);
        Tkinter.Radiobutton(frame, text='Negativo', variable=self.rb_notice, \
                value=0).pack(side = Tkinter.LEFT);

    def __init_button(self):
        frame = Tkinter.Frame(self.tk);
        frame.pack();
        Tkinter.Button(frame, text='Enviar', command=self.__getData).pack();

    def __getData(self):
        pass

    def start_fuzzy(self, stock_file, fuzzy_file):
        self.smf.read_file(stock_file);
        self.tk.mainloop();

if __name__ == '__main__':
    if (len(argv) > 2):
        tkf = TkinterFuzzy();
        tkf.start_fuzzy(argv[1], argv[2]);
