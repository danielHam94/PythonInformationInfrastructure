from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self, text = "Light is: OFF", command = self.toggle)
        self.bttn.grid()
 
    def toggle(self):
        if self.bttn["text"] == "Light is: ON":
            self.bttn["text"] = "Light is: OFF"
        else:
            self.bttn["text"] = "Light is: ON"

# main
root = Tk()
root.title("Light Switch Button")
root.geometry("250x25")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()

