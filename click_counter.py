from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Click to increment!")
        self.lbl.grid()
        self.bttn = Button(self)
        self.bttn["text"]= "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
 
    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main
root = Tk()
root.title("Click Counter")
root.geometry("250x75")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
