# Import tkinter library 
import tkinter as tk

#Created function for button click and print it
def button_click():
    print("Button clicked!")
#Create class library with root window
root = tk.Tk()
root.title("Button Example")
    
#Create the button object with 3 different arguments 
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

#Call the main root main loop
root.mainloop()
