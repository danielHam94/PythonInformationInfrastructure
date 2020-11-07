from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="This is a label!")
        self.lbl.grid()
        self.bttn1 = Button(self, text = "I do nothing!")
        self.bttn1.grid()


# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
