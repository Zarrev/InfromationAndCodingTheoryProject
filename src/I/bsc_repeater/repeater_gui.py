from tkinter import *
from tkinter.ttk import *
from I.bsc_repeater.repeater_model import process
import re


class StrRestrictionEntry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        self.set(''.join([self.get()[i] if not re.match("[2-9a-zA-Z]", self.get()[i]) else ''
                          for i in range(len(self.get()))]))


class TransGUI:

    def __init__(self, window, _click):
        self.lbl = Label(window, text="Transmitter side")
        self.lb2 = Label(window, text="Binary \nmessage:", width=8)
        self.txt1 = StrRestrictionEntry(window, width=10)
        self.btn1 = Button(window, text="Send", command=_click, width=7)
        self.combo = Combobox(window, width=5)
        self.combo['values'] = (1, 3, 5, 7, 9, 12)
        self.combo.current(1)
        self.lb3 = Label(window, text="Coded\nmessage:\n", width=8)
        self.lb4 = Label(window, text="None", width=8)
        self.lb5 = Label(window, text="Repeat\nnumber:", width=8)
        self.set_grids()

    def set_grids(self):
        self.lbl.grid(column=1, row=0)
        self.lb2.grid(column=0, row=1)
        self.txt1.grid(column=1, row=1)
        self.btn1.grid(column=1, row=2)
        self.lb5.grid(column=0, row=3)
        self.combo.grid(column=1, row=3)
        self.lb3.grid(column=0, row=4)
        self.lb4.grid(column=1, row=4)


class ChanGUI:

    def __init__(self, window):
        self.lb1 = Label(window, text="Channel")
        self.lb2 = Label(window, text="Bit error \nprob.:\n", width=8)
        self.combo = Combobox(window, width=5)
        self.combo['values'] = (0.1, 0.2, 0.3, 0.4, 0.5)
        self.combo.current(1)
        self.lb3 = Label(window, text="Error \nvec.:\n", width=8)
        self.lb4 = Label(window, text="None", width=8)
        self.set_grids()

    def set_grids(self):
        self.lb1.grid(column=3, row=0)
        self.lb2.grid(column=2, row=1)
        self.combo.grid(column=3, row=1)
        self.lb3.grid(column=2, row=2)
        self.lb4.grid(column=3, row=2)


class RecGUI:

    def __init__(self, window):
        self.lb1 = Label(window, text="Receiver side")
        self.lb2 = Label(window, text="Received msg.:")
        self.lb3 = Label(window, text="None")
        self.lb4 = Label(window, text="Decoded msg.:")
        self.lb5 = Label(window, text="None")
        self.set_grids()

    def set_grids(self):
        self.lb1.grid(column=5, row=0)
        self.lb2.grid(column=4, row=1)
        self.lb3.grid(column=5, row=1)
        self.lb4.grid(column=4, row=2)
        self.lb5.grid(column=5, row=2)


def _quit():
    window.quit()


def click():
    msg = t.txt1.get()
    repeat = int(t.combo.get())
    prob = float(c.combo.get())
    coded, err_vec, sent, decoded = process(msg, repeat, prob)
    t.lb4.configure(text=coded)
    c.lb4.configure(text=err_vec)
    r.lb3.configure(text=sent)
    r.lb5.configure(text=decoded)


window = Tk()
window.title("Welcome to the ErrorCorrection World")
window.geometry('450x300')

t = TransGUI(window, click)
c = ChanGUI(window)
r = RecGUI(window)

btn = Button(window, text="Quit", command=_quit)
btn.grid(column=5, row=7)

window.mainloop()