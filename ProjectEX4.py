#EXAMPLE 4
#Here, again, I am improting the random library into my program so that I will be able to use 
#the choice function
import random
#Here is my dictionary for the yellow strip level Korean Taekwon-Do terms and their English equivalents. 
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

#Below, my program prints an intoducotry phase so that the user knows what the program does. 
print("In the following program, you will be translating Taekwon-Do\nterms from Korean to English!")
print("")
#Here, I start a loop, the loop wil run in range 5, or 5 times, bumping the value of x up 1 each time
#It will start at x=0, since python always starts everything from 0, and will go up to 4, 
#with the 5 not included.
for x in range(5):
    question = random.choice(list(my_dict)) #the question variable is a random choice (key) 
                                            #from the dictionary
    #Here, the answer variable is the user input to the question asking for the translation 
    #of the question variable, or the random key (word in english)
    answer = input("What is the Korean translation of " + question + "?\n")
    
    #Below I used conditionals, or if/elif/else statements, saying that if the answer variable is 
    #equal to the value of the question part of the dictionary, print CORRECT. 
    if answer == my_dict[question]:
        print("CORRECT!")
    #If the above mentioned is not true (else), the program will print INCORRECT, and state the correct
    #answer (or the value of the question key from the dictionary)
    else: 
        print("Sorry, INCORRECT")
        print("The correct answer would have been " + my_dict[question])