from Tkinter import Tk, Button
from tkFont import Font


class GUI:

    def __init__(self):

        self.app = Tk()
        self.app.title = 'Hounds and Hares'

    def mainloop(self):
        self.app.mainloop()

if __name__ == "__main__":
    GUI().mainloop()
