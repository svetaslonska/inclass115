#Going to the library and import tkinter library and ttk
import tkinter as tk
from tkinter import ttk

#Create a function for the event
def on_select(event):

    #Create an item object that obtains the value of selected item
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
 
#Create the root window 
root = tk.Tk()
root.title("Sveta")

#Create an array with the number of items 
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#Create a combo box object, put the object in the root window and populate values
combo_box = ttk.Combobox(root, values=items)

#Create binding function which will tie the selected item to the on_selected function
combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the object to the screen with the Geometry manager
combo_box.pack()

#Run the main looop function which keeps the root parent window visible
root.mainloop()