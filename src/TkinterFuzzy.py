#!/usr/bin/python

from StockMarketFuzzy import *
import Tkinter
import tkMessageBox

class TkinterFuzzy:
    def __init__(self):
        self.tk = Tkinter.Tk();
        self.tk.title('Stock Market Fuzzy');
        self.tk.resizable(0, 0);
        self.__init_option_file();
        self.__init_entries();
        self.__init_entries_news();
        #self.__init_radiobuttons();
        self.__init_button();
        self.smf = StockMarketFuzzy();

    def __init_option_file(self):
        self.option_value = Tkinter.IntVar();
        Tkinter.Checkbutton(self.__get_frame(), text='Usar arquivo', variable=self.option_value, \
                command=self.__set_entries).pack();

    def __set_entries(self):
        if (self.option_value.get()): self.__disable_entries();
        else: self.__enable_entries();

    def __disable_entries(self):
        self.e_mm10.configure(state = Tkinter.DISABLED);
        self.e_mm50.configure(state = Tkinter.DISABLED);
        self.e_real.configure(state = Tkinter.DISABLED);

    def __enable_entries(self): 
        self.e_mm10.configure(state = Tkinter.NORMAL);
        self.e_mm50.configure(state = Tkinter.NORMAL);
        self.e_real.configure(state = Tkinter.NORMAL);

    def __init_entries(self):
        frame = self.__get_frame();
        Tkinter.Label(frame, text='Media movel 10 dias:').pack(side = Tkinter.LEFT);
        self.e_mm10 = Tkinter.Entry(frame, bd=5);
        self.e_mm10.pack(side = Tkinter.LEFT);
        
        frame = self.__get_frame();
        Tkinter.Label(frame, text='Media movel 50 dias:').pack(side = Tkinter.LEFT);
        self.e_mm50 = Tkinter.Entry(frame, bd=5);
        self.e_mm50.pack(side = Tkinter.LEFT);

        frame = self.__get_frame();
        Tkinter.Label(frame, text='Valor real:').pack(side = Tkinter.LEFT);
        self.e_real = Tkinter.Entry(frame, bd=5);
        self.e_real.pack(side = Tkinter.LEFT);

    def __init_entries_news(self):
        frame = self.__get_frame();
        Tkinter.Label(frame, text='Total de noticias:').pack(side = Tkinter.LEFT);
        self.e_total_news = Tkinter.Entry(frame, bd=5);
        self.e_total_news.pack(side = Tkinter.RIGHT);

        frame = self.__get_frame();
        Tkinter.Label(frame, text='Noticias positivas:').pack(side = Tkinter.LEFT);
        self.e_positive_news = Tkinter.Entry(frame, bd=5);
        self.e_positive_news.pack(side = Tkinter.RIGHT);


    def __init_radiobuttons(self):
        frame = self.__get_frame();
        Tkinter.Label(frame, text='Noticia:').pack(side = Tkinter.LEFT);
        self.rb_notice = Tkinter.IntVar();
        Tkinter.Radiobutton(frame, text='Positivo', variable=self.rb_notice, \
                value=1).pack(side = Tkinter.LEFT);
        Tkinter.Radiobutton(frame, text='Negativo', variable=self.rb_notice, \
                value=0).pack(side = Tkinter.LEFT);

    def __init_button(self):
        Tkinter.Button(self.tk, text='Enviar', command=self.__getData).pack();

    def __getData(self):
        mm10 = mm50 = real = total_news = positive_news = 0;
        if (not self.option_value.get()):
            try:
                mm10 = float(self.e_mm10.get());
                mm50 = float(self.e_mm50.get());
                real = float(self.e_real.get());
            except Exception as error:
                tkMessageBox.showerror('Dados invalidos', 'Insira um numero nos campos');
                return;
        else:
            mm10 = self.smf.moving_average(90, 100);
            mm50 = self.smf.moving_average(50, 100);
            real = self.smf.get_real(100);
        try:
            total_news    = float(self.e_total_news.get());
            positive_news = float(self.e_positive_news.get());
            if (positive_news > total_news):
                tkMessageBox.showerror('Erro', 'Quantidade de noticias positivas maior do que o total');
                return;
        except Exception as error:
            tkMessageBox.showerror('Dados invalidos', 'Insira um numero nos campos');
            return;
        news = float('{0:.3f}'.format(positive_news / total_news));
        mm10_diff = float('{0:.3f}'.format(abs(mm10 - real) / real));
        mm50_diff = float('{0:.3f}'.format(abs(mm50 - real) / real));
        if (mm10_diff > 1): mm10_diff = 1;
        if (mm50_diff > 1): mm50_diff = 1;
        result   = self.smf.fuzzy(self.fuzzy_file, mm10_diff, mm50_diff, news);
        message  = 'MM 10: ' + str(mm10) + '\nMM 50: ' + str(mm50) \
                + '\nReal: ' + str(real) + '\nNoticias positivas: ' + str(news * 100) \
                + '%\nMM 10 Diferenca: ' + str(mm10_diff * 100) \
                + '%\nMM 50 Diferenca: ' + str(mm50_diff * 100) \
                + '%\nResultado: ' + str("%.2f" % (result * 100)) + '%';
        self.__display_message(message);

    def __get_frame(self):
        frame = Tkinter.Frame(self.tk);
        frame.pack(anchor = Tkinter.W);
        return frame;

    def __display_message(self, message):
        tkMessageBox.showinfo('Resultado', message);

    def set_fuzzy_file(self, fuzzy_file):
        self.fuzzy_file = fuzzy_file;

    def start_fuzzy(self, stock_file):
        self.smf.read_file(stock_file);
        self.tk.mainloop();

if __name__ == '__main__':
    if (len(argv) > 2):
        tkf = TkinterFuzzy();
        tkf.set_fuzzy_file(argv[2]);
        tkf.start_fuzzy(argv[1]);
    else:
        print "Insira o arquivo com 100 dias de dados e o codigo fuzzy."
