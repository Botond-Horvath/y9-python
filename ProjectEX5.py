#I am importing the random library
import random
#My yellow stripe dictionary.
my_dict = {
	 "four direction punch:": "saju jirugi",
    "four direction block:": "saju makgi",
    "attention stance:": "charyot sogi",
    "bow posture:": "kyongye jase",
    "parallel stance": "narani sogi",
    "parallel ready stance:": "narani junbi sogi",
    "walking stance:": "gunnun sogi",
    "walking stance middle front punch:": "gunnun so kaunde ap jirugi",
    "walking stance outer forearm low block:": "gunnun so bakat palmok najunde makgi",
    "walking stance knife-hand low block:": "gunnun so sonkal najunde makgi",
    "walking stance inner forearm middle side block:": "gunnun so an palmok kaunde yop makgi",
    "front rising kick:": "apcha olligi",
    "front snap kick:": "apcha busigi",
    "free sparring:": "jayu matsogi",}
#Below is the explanation of the program to the user. 
print("OK, you will be writing a full test for yellow strip Taekwon-Do definitions!")
print("")
#Here, I made the 'cont' variable the integer of the input of the user to the below specified command.
#If that command is 1, (which means continue), then continue with the program... 
cont = int(input("Please enter 1 if you are ready to contine with no spaces... \n"))
if cont == 1:
	#Here, the loop begins for range 14 (amout of pairs in the yellow strip dictionary.)
	for x in range(14):
		question = random.choice(list(my_dict))
		answer = input("What is the Korean translation of " + question + "?\n")
		if answer == my_dict[question]:
			print("CORRECT!")
		else: 
			print("Sorry, INCORRECT")
			print("The correct answer is " + my_dict[question] + "...")
		#Below is something new, since the 'test' function will not have any repeats. 
		#So, the '.pop' function removes the question variable (random key) from the dictionary
		my_dict.pop(question)
#If the user does not type 1, they get an error message and need to leave the program. 
else:
	print("Sorry, that is not a valid answer... ")
	print("Press enter to leave the program. ")
