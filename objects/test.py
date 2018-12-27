from tkinter import *
from functools import partial

master = Tk()
master.geometry("500x500")

global poop

class Poop:

    def __init__(self):
        self.poop = True

    def set_poop(self, obje):
        self.poop = obje
        master.destroy()


poop = Poop()




def callback():
    poop = False


b = Button(master, text="OK", command=partial(poop.set_poop, "Johnny"))

b.pack()

mainloop()

print(poop.poop)




