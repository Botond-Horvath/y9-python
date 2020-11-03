#EXAMPLE 6
#Below is the information about the program for the user: 
print("")
print("Welcome to the demonstration of how while loops work! ")
print("Please answer the following questions... ")
print("")

#Here, I am sepcifying 'gup' to be the user input as an integer from the question about their 'gup' level. 
gup = int(input("What is your gup level that you are preparing to grade for? \n"))
#Now, I enter a while loop, that states that if the gup entered is not something from 1-9,
#It should contine printing that that is not a valud answer, and asking the user again. 
while gup < 1 or gup > 9:
	gup = int(input("Please type in a valid gup level \n"))

#The same process as above is repreated below for the translation order and test type, 
#Here, the valid answers are 1 or 2. 
translate = int(input("Type in 1 for Korean to English and 2 for English to Korean! \n"))
while not (translate == 1 or translate == 2):
	translate = int(input("Please type in a valid number \n"))

test = int(input("Press 1 for a pop-quiz and 2 for a full test... \n"))
while not (test == 1 or test == 2):
	test = int(input("Please type in a valid number \n"))
