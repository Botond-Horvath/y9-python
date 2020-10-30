#This program takes 5 user input names, and adds them to a list that it prints for the user. 
#Author: Botond Horvath
#October 29th, 2020

#Explanation to the user of what they should do: 
print("This program lets the user type in the name of 5 people, \nand adds these names to a list! ")
print("") #Extra space (neatness)
name_list = [] #The list here is empty, ready for the names to be added. 

#Here, a loop will run 5 times with the contents indented in it:
for name in range(5):
	name = input("Type in the name: \n") #Name variable becomes the input name from the user. 
	name_list.append(name) #That name will be added to the empty list, and the loop will repeat for 5 names. 

#At the end, the program prints that the list of the user's names is, and then the string of the list. 
print("Your list of names is: " + str(name_list))
