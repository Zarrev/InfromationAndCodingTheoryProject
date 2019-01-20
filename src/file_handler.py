from tkinter import *
from tkinter import filedialog
from os import getcwd

filename = 'UNNAMED'


def get_file(title="Select a file for the operation!"):
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
        print('unhex:', data)
        print('hex:', bytes.fromhex(data))
        open(directory + '/' + new_filename, "wb").write(bytes.fromhex(data))
        return 'Your encrypted file has saved!'
    except Exception as e:
        print('Actual error: {0}'.format(e))
    root.destroy()
