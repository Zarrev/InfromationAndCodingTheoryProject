from tkinter import *
from tkinter import ttk, messagebox
from III import otp_model as om, file_handler as fh, rsa_model as rm

"""
This script makes the GUI. We can execute all function what I implemented i.e. RSA and OTP cryptography algorithm.
I used for it the 'tkinter' what the part of standard library. I implemented the event functions below, and made a new
class for the restriction of input field for accept only the numbers.
"""


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

    def get_in_int(self):
        if len(self.get()) > 0:
            return int(self.get())

        raise Exception('First you have to give a prime number!')


def open_btn_click():
    selected_tab = tab_control.tab(tab_control.select(), "text")
    if selected_tab == 'OTP':
        loaded_file = fh.get_file()
        if loaded_file is not None:
            otp.set_input(loaded_file)
    else:
        loaded_file = fh.get_file(rsa=True)
        if loaded_file is not None:
            rsa.set_input(loaded_file)


def save_btn_click():
    selected_tab = tab_control.tab(tab_control.select(), "text")
    if selected_tab == 'OTP':
        save = otp.get_output()
    else:
        save = rsa.get_output()

    if save:
        if selected_tab == 'OTP':
            fh.save_encrypted_file(save)
        else:
            fh.save_encrypted_file(save, rsa=True)
    else:
        messagebox.showwarning('Warning!', 'You do not have any output!')


def generate_key():
    selected_tab = tab_control.tab(tab_control.select(), "text")
    if selected_tab == 'OTP':
        otp.set_key()
        fh.save_key(otp.get_key(), 'otp_key')
    else:
        try:
            fh.save_keys(rsa.get_key(txt1.get_in_int(), txt2.get_in_int()))
        except Exception as e:
            messagebox.showwarning('Warning!',
                                   'You cannot complete this action until you do not give two number (prime)!')
            print(e)


def load_key():
    selected_tab = tab_control.tab(tab_control.select(), "text")
    if selected_tab == 'OTP':
        loaded_key = fh.load_key()
        if loaded_key is not None:
            otp.set_key(loaded_key)
    else:
        loaded_key = fh.load_key(_tuple=True)
        if loaded_key is not None:
            rsa.set_key(loaded_key, selected.get())


def start():
    try:
        selected_tab = tab_control.tab(tab_control.select(), "text")
        if selected_tab == 'OTP':
            otp.set_output(selected.get())
        else:
            rsa.set_output(selected.get())
    except Exception as e:
        print(e)
        messagebox.showwarning('Warning!', 'You cannot complete this action yet!')


def _quit():
    window.quit()


otp = om.OTP_M()
rsa = rm.RSA_M()
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('450x300')

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
btn3 = Button(tab2, text="Open your input file", command=open_btn_click)
btn4 = Button(tab2, text="Save your output file", command=save_btn_click)
btn5 = Button(tab1, text="Generate key and save", command=generate_key)
btn6 = Button(tab2, text="Generate keys and save", command=generate_key)
btn7 = Button(tab1, text="Start", command=start)
btn8 = Button(tab2, text="Start", command=start)
btn9 = Button(tab1, text="Quit", command=_quit)
btn10 = Button(tab2, text="Quit", command=_quit)
btn11 = Button(tab1, text="Load your key", command=load_key)
btn12 = Button(tab2, text="Load a key", command=load_key)

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

tab_control.pack(expand=1, fill='both')
window.mainloop()
