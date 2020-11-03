#from TKinter, I am importing everything. 
from tkinter import *

#I open a new TKinter window, I set the geometry of that window, and set the title of the window. 
window = Tk()
window.geometry('400x200')
window.title('Taekwon-Do Quiz')

#I make 'count' an ineger variable with the value 0. 
count = IntVar(value=0)

#I define buttonFunction here as setting the count variable to getting the value of it (0) and adding 1.
#This function will only run if a command is given to run buttonFunction. 
def buttonFunction(): 
	count.set(count.get() + 1)

#I make b1 a button in the window, set a text on it, and a command for what to do when it is pressed. 
#When it is pressed, the command leads to the function above, giving an output of 1.
b1 = Button(window, text=('Press to learn counting!'), command=buttonFunction)
b1.pack() #prints the button. 

#The above value of 1 has to be printed, so I made l1 a new label in the window. 
#The lable will print (pack) the text inside the count variable (1)
l1 = Label(window, textvariable=count)
l1.pack()

#Every time b1 is pressed, the number shown will increase by 1: (1,2,3,4,5,6,7 etc.)

#.mainloop keeps the window open until the user closes it. 
window.mainloop()
