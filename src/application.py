from tkinter import *
from tkinter import ttk
import file_handler as fh
import otp_modell as om


class IntegerEntry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit() or self.get() == '':
            self.old_value = self.get()
        else:
            self.set(self.old_value)


def open_btn_click():
    otp.set_input(fh.get_file())


def save_btn_click():
    fh.save_encrypted_file(otp.get_output())


def generate_key():
    otp.set_key()
    fh.save_key(otp.get_key(), 'otp_key')


def load_key():
    otp.set_key(fh.load_key())


def start():
    otp.set_output(selected.get())


def quit():
    window.destroy()

otp = om.OTP_M()
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='OTP')
tab_control.add(tab2, text='RSA')

selected = IntVar()
selected.set(1)
rad1 = Radiobutton(tab1, text='Encryption', value=1, variable=selected)
rad2 = Radiobutton(tab1, text='Decryption', value=2, variable=selected)
rad3 = Radiobutton(tab2, text='Encryption', value=1, variable=selected)
rad4 = Radiobutton(tab2, text='Decryption', value=2, variable=selected)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=0, row=0)
rad4.grid(column=1, row=0)

lbl = Label(tab2, text="First prime number")
lb2 = Label(tab2, text="Second prime number")
lbl.grid(column=0, row=3)
lb2.grid(column=0, row=4)

txt1 = IntegerEntry(tab2, width=10)
txt2 = IntegerEntry(tab2, width=10)
txt1.grid(column=1, row=3)
txt2.grid(column=1, row=4)

btn1 = Button(tab1, text="Open your input file", command=open_btn_click)
btn2 = Button(tab1, text="Save your output file", command=save_btn_click)
btn3 = Button(tab2, text="Open your input file", command=open_btn_click) # TODO
btn4 = Button(tab2, text="Save your output file", command=save_btn_click) # TODO
btn5 = Button(tab1, text="Generate key", command=generate_key)
btn6 = Button(tab2, text="Generate keys", command=generate_key) # TODO
btn7 = Button(tab1, text="Start", command=start)
btn8 = Button(tab2, text="Start", command=start) # TODO
btn9 = Button(tab1, text="Quit", command=quit)
btn10 = Button(tab2, text="Quit", command=quit)
btn11 = Button(tab1, text="Load your key", command=load_key)
btn12 = Button(tab2, text="Load your private key", command=load_key) # TODO
btn13 = Button(tab2, text="Load the public key", command=load_key) # TODO

btn1.grid(column=0, row=1)
btn2.grid(column=0, row=2)
btn3.grid(column=0, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=4, row=2)
btn6.grid(column=4, row=2)
btn7.grid(column=4, row=3)
btn8.grid(column=4, row=3)
btn9.grid(column=4, row=4)
btn10.grid(column=4, row=4)
btn11.grid(column=0, row=3)
btn12.grid(column=1, row=1)
btn13.grid(column=1, row=2)

tab_control.pack(expand=1, fill='both')
window.mainloop()