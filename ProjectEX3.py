#EXAMPLE 3
#Below, I am importing the random library of python to my program
#With this, I will be able to use actions, like 'choice' from the random library.
import random
#Below is my dictionary with keys and values for Taekwon-Do terms in Korean and English.
#All of the dictionary is stored in the variable: "my_dict"
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
     "free sparring:": "jayu matsogi"}
#Below, I am using the choice function from the random library
#I am selecting a random choice from the dictionary (remember, this is default to be the key)
#The dictionary has to be transformed into a list in order for this program to work. 
question = random.choice(list(my_dict))
#The program prints a question about the Korean translation of the question variable (the random key)
print("What is the Korean translation of " + question + "?")
#Below, the answer variable gets assigned the value of the question variable (a random key)
answer = my_dict[question]
#It prints that the answer to the above question for the random key translation would be 
#the answer variable
print("Well, the answer would be: " + answer + "!")
