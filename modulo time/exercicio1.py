from tkinter import *
import time


class Hour(object):
    def __init__(self):
        self.ins = Tk()
        self.ins.geometry('300x300')
        self.ins.resizable(False, False)
        self.ins['bg'] = 'black'
        self.interface()
        self.ins.mainloop()

    def interface(self):
        frame1 = Frame(self.ins, borderwidth=0, bg='black')
        frame1.pack(side=BOTTOM)

        self.canva = Canvas(frame1, width=300, height=200, bg='black')
        self.canva.pack()
        self.canva.create_rectangle(100,80,200,180, fill='white')
        bot = Button(frame1, text='HOUR NOW', borderwidth=0, command=self.hora)
        bot.pack()

    def hora(self):
        self.canva.after(10,self.hora)
        self.hora1()
        self.refaz()

    def hora1(self):
        horas = time.localtime()
        self.canva.create_text(150,135, text=f'{horas[3]}:{horas[4]}:{horas[5]}', fill='orange')

    def refaz(self):
        self.canva.delete(ALL)
        self.canva.create_rectangle(100, 80, 200, 180, fill='white')
        horas = time.localtime()
        self.canva.create_text(150, 135, text=f'{horas[3]}:{horas[4]}:{horas[5]}', fill='orange')


if __name__ == '__main__':
    Hour()
