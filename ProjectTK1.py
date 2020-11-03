#from TKinter, I am importing everything. 
from tkinter import *

#I open a new TKinter window, I set the geometry of that window, and set the title of the window. 
window = Tk()
window.geometry('800x500')
window.title('Taekwon-Do Quiz')

# I make a Tkinter str variable (greeting)
greeting = StringVar()

#Make l1 a label in the TKinter window, saying the welcome text. Then, I pack (print) that. 
l1 = Label(window, text=('Welcome to the Taekwon-Do translator!'))
l1.pack()

#I define printGreeting as setting the greeting variable to 'welcome, you are in.' 
#greeting is already a string variable as specified above. 
#This finction will only rin if a command is given for 'printGreeting' to run.
def printGreeting(): 
	greeting.set("Welcome! You are in.")

#I make b1 button in the window, specify the text on it, and the command (what happens when pressed)
#the command leads to the function above setting greeting to the welcome text.
b1 = Button(window, text=('Press to START!'), command=printGreeting)
b1.pack() #Prints the button.

#I can make l2 a new label in the window, contianing the text in the variable: greeting. 
#Greeting is the variable specified above when the button is pressed, 
#so this label prints when button is pressed
l2 = Label(window, textvariable=greeting)
l2.pack() #prints the label (only when button pressed). 

#This mainloop command just keeps the window open until the user closes it. 
window.mainloop()