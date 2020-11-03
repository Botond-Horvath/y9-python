#EXAMPLE 2
#Below, we are printing an introductory string (strings are in quotations).
print("This program calculates the average of 3 numbers! ")
#Below, we take the integer forms of 3 user inputs, store them in variables, 
#and then print them added to strings as strings.
num1 = int(input("What is your first number? \n"))
print("Your first number is " + str(num1))
num2 = int(input("What is your second number? \n"))
print("Your second number is " + str(num2))
num3 = int(input("What is your third number? \n"))
print("Your third number is " + str(num3))
#Here, we take the float form of the calculated average (3 user input integers 
#added up and divided by 3 to get the mean), since averages can be decimals, 
#and store them in the average variable.
average = float((num1 + num2 + num3)/3) 
#Below, we print 'your average is' and the average float in the form of a string (scentence).
print("Your average is: " + str(average))