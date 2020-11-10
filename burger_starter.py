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

        Radiobutton(self, text = "Rare", variable = self.level,
                    value = "rare").grid()

        Radiobutton(self, text = "Medium", variable = self.level,  value = "medium").grid()

        Radiobutton(self, text = "Well-done", variable = self.level,  value = "well-done").grid()

        Button(self, text = "Place order", command = self.order_burger).grid()

        self.results_txt = Text(self, width = 70, height = 2, wrap = WORD)
        self.results_txt.grid()

    def order_burger(self):
        # When the user clicks 'Place order', the burger they chose
        # should be output to the results text box.
        # Show the cooking level and cheese option.
        pass

# main
root = Tk()
root.title("Order a Burger")
root.geometry("450x300")
app = Application(root)
root.mainloop()
 
