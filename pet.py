# Pet Chooser 
# Demonstrates radio buttons

from tkinter import *

class Application(Frame):
    """ GUI Application for favorite pet type. """
    def __init__(self, master):

        """ Initialize Frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for pet type choices. """
        # create description label
        Label(self,
              text = "Choose your favorite type of pet"
              ).grid(row = 0, column = 0, sticky = W)

        # create instruction label
        Label(self,
              text = "Select one:"
              ).grid(row = 1, column = 0, sticky = W)

        # create variable for single, favorite type of pet
        self.favorite = StringVar()
        self.favorite.set(None)

        # create Dogs radio button
        Radiobutton(self,
                    text = "Dogs",
                    variable = self.favorite,
                    value = "dogs",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # create Cats radio button
        Radiobutton(self,
                    text = "Cats",
                    variable = self.favorite,
                    value = "cats",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        # create Hampster radio button
        Radiobutton(self,
                    text = "60-foot tall radioactive hampsters",
                    variable = self.favorite,
                    value = "Hampsterzilla",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # create text field to display result
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """ Update text area and display user's favorite pet type. """
        message = "Your favorite type of pet is "
        message += self.favorite.get()
        message += "."

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

# main
root = Tk()
root.title("Pet Chooser")
app = Application(root)
root.mainloop()
        
