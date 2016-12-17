import os
from tkinter import *
import tkinter.filedialog as fdial
def set_text(text):
    e.delete(0,END)
    e.insert(0,text)
    return
def directory():
	dire=fdial.askdirectory()
	e.delete(0,END)
	e.insert(0,dire)

def replace():
	way=e.get()
	fname=os.listdir(way)
	for f in fname:
		if tr.get() in f:
			a=way+'/'+f.replace(tr.get(),rw.get())
			b=way+'/'+f
			os.rename(b,a)
				

win = Tk()

e = Entry(win,width=10)
e.pack()

b1 = Button(win,text="browse",command=directory)
b1.pack()

tr=Entry(win,width=10)
tr.pack()
rw=Entry(win,width=10)
rw.pack()

b1 = Button(win,text="Replace",command=replace)
b1.pack()

win.mainloop()