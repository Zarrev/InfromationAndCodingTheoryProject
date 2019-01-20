from tkinter import *
from tkinter import filedialog
from os import getcwd

"""
This global variable is exist for keep the file's name if we need it later.
"""
filename = 'UNNAMED'


def get_file(title="Select a file for the operation!"):
    """
    This function read the chosen file with the tkinter library what gives the GUI part of this function.
    :param title: Optional parameter, we can redefine the title of the pop-up window.
    :return:
    """
    global filename
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir=getcwd(), title=title)
    filename = root.filename.split(sep='/')[-1]
    data = None
    try:
        data = open(root.filename, "rb").read()
    except Exception as e:
        print('Something went wrong. :(')
        print('Actual error({0}): {1}'.format(e.errno, e.strerror))
    root.destroy()

    return data.hex()


def save_encrypted_file(data, new_filename=None, title="Select a directory for your file!"):
    """
    This function save your encrypted data.
    :param data: That data what you encrypted (the data has hexadecimal encoding).
    :param new_filename: Optional parameter, with this you can redefine your file name.
    :param title: Optional parameter, we can redefine the title of the pop-up window.
    :return:
    """
    global filename
    if new_filename is None:
        new_filename = 'en_' + filename
    else:
        new_filename = filename
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir=getcwd(), title=title)
    try:
        if directory == '':
            raise Exception('You did not choose any directory for saving.')
        open(directory + '/' + new_filename, "wb").write(bytes.fromhex(data))
        return 'Your encrypted file has saved!'
    except Exception as e:
        print('Actual error: {0}'.format(e))
    root.destroy()


def save_key(key, name_of_file):
    """
    With this methode, you can save your key into a .txt file.
    :param key: your key what comes from another function or class.
    :param name_of_file: use for name your key's file.
    """
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir=getcwd(), title="Selec a dictionary for your file!")
    try:
        if directory == '':
            raise Exception('You did not choose any directory for saving.')
        open(directory + '/' + name_of_file + '.txt', "w").write(key)
        return 'Your encrypted file has saved!'
    except Exception as e:
        print('Actual error: {0}'.format(e))
    root.destroy()


def load_key():
    """
    This function loads your key from a file.
    :return:
    """
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir=getcwd(), title='Select your key_file!')
    data = None
    try:
        data = open(root.filename, "r").read()
    except Exception as e:
        print('Something went wrong. :(')
        print('Actual error({0}): {1}'.format(e.errno, e.strerror))
    root.destroy()

    return data
