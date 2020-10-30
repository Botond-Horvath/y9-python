#This program calculates the average of 5 numbers that the user tyes in
#Author: Botond Horvath
#October 29th, 2020

total = 0.0 #Assignes the value of 0.0 (a float) to the total variable
#prints introdutory phases for the user here: 
print("Welcome to the average calculator!")
print("")
print("This calculator will calculate the average of 5 numbers:") 
#Creates a loop that will run 5 times: 
for numbers in range(5):
	mynum = int(input("Type in your score below: \n")) #mynum varaible is assigned to the integer that the user enters. 
	print("Ok, your number is: " + str(mynum)) #prints confirmation scentence for the users number. 
	total = total + mynum #reassignes the value of total (0) to total (0) + mynum, so basically "mynum"
print("Your average score is: ")
print(float(total/5))

#After running the program 5 times, the total will be the sum of the 5 intigers entered.
#Then, the program will print the average, in a float of the sum (total) divided by 5 (mean value)