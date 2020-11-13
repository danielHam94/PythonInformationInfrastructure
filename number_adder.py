from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "Enter two numbers: ")
        self.lbl.grid()
        self.ent_one = Entry(self, width=30)
        self.ent_one.grid()
        self.ent_two = Entry(self, width=30)
        self.ent_two.grid()
        self.sum_lbl = Label(self, text="The sum: ")
        self.sum_lbl.grid()
        self.bttn = Button(self)
        self.bttn["text"]= "Add Numbers"
        self.bttn["command"] = self.add
        self.bttn.grid()
        
    def add(self):
        try:
            total = str(eval(self.ent_one.get()) + eval(self.ent_two.get()))
            self.sum_lbl["text"] = "The sum: " + total
        except:
            self.sum_lbl["text"] = "Error: invalid value."            
        self.ent_one.delete(0, END)
        self.ent_two.delete(0, END)

# main
root = Tk()
root.title("Simple Adder")
root.geometry("200x110")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
