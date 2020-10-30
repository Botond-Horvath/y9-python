#This program gives the user 10 tries to guess a number between 1 and 20. 
#Author: Botond Horvath
#October 29th, 2020
number = 14 #Assignes the value of 14 to the number (this is the number the user will have to guess).
#The program prints the information of what the user will have to go below:
print("You have to guess a number between 1 and 20, and have 10 attempts! ")
print("") #Extra space (neatness)
#Below is a loop, where it will run the program indented in it 10 times. 
for num in range(10):
	mynum= float(input("What is the number?\n")) #Assignes the float that the user inputes to (mynum) variable. 
	#The float is so that the program does not crash in casse of a decimal. 
	if mynum == number: #If the user input is the same as number (14), print the congrats.
		print("You guessed it! Well done! ") 
		break #This breaks the loop so that it doesn't ask the question after the number is guessed. 
	elif mynum < 14:
		print("Sorry, but the number is higher that that... ")
	elif mynum > 14:
		print("Sorry, but the number is lower than that... ")
	else: 
		print("Sorry, that is not a valid answer... ")
		#Range of conditional statements: if user input is less than 14, say that they need to type higher.
		#If user input is more than 14, print that the number is lower. 
print("The number was: 14! ")
#after the user guesses the number (loop is broken), or if they cannot guess it (loop ends), print what the number was. 
