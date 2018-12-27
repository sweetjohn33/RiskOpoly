from tkinter import *

class Menu:

    def __init__(self, titles, commands):
        self.titles = titles
        self.commands = commands

    def menu(self):
        new_window = Tk()
        new_window.geometry("500x500")

        for i in range(len(self.titles)):
            b = Button(new_window, text=self.titles[i], command=self.commands[i])
            b.pack()

        mainloop()

def pint():
    print("hellow world")


monopoly = Menu(["buy house", "turn in cards", "mortgage"], [pint, pint, pint])
monopoly.menu()


