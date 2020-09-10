from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

win = tk.Tk()
win.title('Image converter')


pathOut = '/home/davide/Desktop'

def openfile():
    global pathIn
    pathIn = filedialog.askopenfilename(title='Chose File', filetypes=[('All files','.*')])

def convert():
    img = Image.open(pathIn)
    img.save(pathOut + '/output' + ext.get())

B1 = tk.Button(text='Scegli file', command=openfile)
B1.grid(row=1, column=0, sticky='WE', padx=20, pady=10)

B2 = tk.Button(text='Converti', command=convert)
B2.grid(row=1, column=2, sticky='WE', padx=20, pady=10)

Arrow = tk.Label(text='>')
Arrow.grid(row=1, column=1, sticky='WE', pady=10)

L1 = tk.Label(text='Choose format')
L1.grid(row=0, column=3, sticky='WE', padx=10, pady=10)

ext = ttk.Combobox(values=[
                            '.bmp',
                            '.jpg',
                            '.png',
                            '.pdf'])
ext.grid(row=1, column=3, sticky='WE', padx=20, pady=10)

win.mainloop()