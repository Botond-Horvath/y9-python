#This program gives the user 5 attempts at guessing a password. 
#Author: Botond Horvath
#October 29th, 2020

#Here, the variable 'password' becomes the string "password", which is the password the user needs to guess. 
password = ("password")

#Below, the user recieves information of what their task is: 
print("There is only one password to get a prize, and you have 5 attempts at \nguessing that word!")
print("")
print("HINT: it is only one word... ")

#This loop will run through its contenets 5 times, thereby giving the user 5 attempts: 
for word in range(5):
	attempt = input("What is the password? \n") #'attempt' variable is assigned the the input attempt of the user. 
	if attempt == password: #If the user attempt is the same as the password...
		print("Well done, you got a PRIZE!") #Print a congratulation... 
		break #and break the loop so that there are no more attempts, since they are unnesesarry.
	
#If the above is not true, the user has not guessed the password and the loop will continue for 5 runs. 
	else:
		print("Sorry, but that is not correct") #Letting the user know that what they typed in is incorrect. 

#After the loop, whether the user guessed the word (loop broke), or the user got to the end of the 5 trials (loop ended)... 
#the program prints that the password was password.
print("The password was 'password'!" )
