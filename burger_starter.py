from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "How do you want your burger?" ).grid()

        Label(self, text = "Cheese?").grid()

        self.cheese = BooleanVar()
        Checkbutton(self, text = "Yes", variable = self.cheese).grid()

        Label(self, text = "Select a cooking level:").grid()

        self.level = StringVar()
        # The default value should be 'medium' when the program starts!
        # If you don't set a default value, ALL the options will be selected.
        self.level.set("medium")

        Radiobutton(self, text = "Rare", variable = self.level,
                    value = "rare").grid()

        Radiobutton(self, text = "Medium", variable = self.level,  value = "medium").grid()

        Radiobutton(self, text = "Well-done", variable = self.level,  value = "well-done").grid()

        Button(self, text = "Place order", command = self.order_burger).grid()

        self.results_txt = Text(self, width = 70, height = 2, wrap = WORD)
        self.results_txt.grid()

    def order_burger(self):
        message = "Your burger is " + self.level.get()
        if self.cheese.get():
            message += " and has cheese on it."
        else:
            message += " and does not have cheese on it."

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

# main
root = Tk()
root.title("Order a Burger")
root.geometry("450x300")
app = Application(root)
root.mainloop()
 
