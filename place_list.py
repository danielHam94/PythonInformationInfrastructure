from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.list_lbl = Label(self, text="This is a list of places I've lived:")
        self.list_lbl.grid()
        
        self.place1 = Button(self, text="1 - Bloomington, IN")
        self.place1.grid()
        
        self.place2 = Button(self, text="2 - Saipan, MP")
        self.place2.grid()
        
        self.place3 = Button(self, text="3 - Seoul, Korea")
        self.place3.grid()
        

# main
root = Tk()
root.title("Places I've Lived")
root.geometry("220x130")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
