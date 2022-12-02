import pandas as pd

import glob
import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

main_win = tkinter.Tk()
main_win.geometry("165x110")

sahaID=tkinter.StringVar()
main_win.sourceFile2G = ''
main_win.sourceFile3G = ''
main_win.sourceFile4G = ''
main_win.saha = ''

def sec():

	main_win.saha=sahaID.get()
 
	sahaID.set("")


def chooseFile2G():
    main_win.sourceFile2G = filedialog.askopenfilenames(parent=main_win, initialdir= r'C:\Users\ozdemir.demiroz\Desktop\sil', title='Please select a directory')


def chooseFile3G():
    main_win.sourceFile3G = filedialog.askopenfilenames(parent=main_win, initialdir= r'C:\Users\ozdemir.demiroz\Desktop\sil', title='Please select a directory')


def chooseFile4G():
    main_win.sourceFile4G = filedialog.askopenfilenames(parent=main_win, initialdir= r'C:\Users\ozdemir.demiroz\Desktop\sil', title='Please select a directory')


b_chooseFile2G = tkinter.Button(main_win, text = "2G", width = 5, height = 1,bg='blue', command = chooseFile2G)
b_chooseFile2G.place(x = 10,y =10)
b_chooseFile2G.width = 50

b_chooseFile3G = tkinter.Button(main_win, text = "3G", width = 5, height = 1,bg='green', command = chooseFile3G)
b_chooseFile3G.place(x = 60,y =10)
b_chooseFile3G.width = 50

b_chooseFile4G = tkinter.Button(main_win, text = "4G", width = 5, height = 1,bg='purple', command = chooseFile4G)
b_chooseFile4G.place(x = 110,y =10)
b_chooseFile4G.width = 50

name_label = tkinter.Label(main_win, text = 'Saha', font=('calibre',10, 'bold'))
name_label.place(x=10,y=50)

name_entry = tkinter.Entry(main_win,textvariable = sahaID, font=('calibre',10,'normal'),width=14)
name_entry.place(x=50,y=50)

sub_btn=tkinter.Button(main_win,text = 'Seç', command = sec)
sub_btn.place(x=10,y=80)




main_win.mainloop()
print("saha id")
print(main_win.saha)
print()
print("2G dosya:")
print(main_win.sourceFile2G)
print()
print("3G dosya:")
print(main_win.sourceFile3G)
print()
print("4G dosya:")
print(main_win.sourceFile4G)