###Module 2.1###
 ###ListTest.py####

"""
    ##liste over navn
name_list = ["karl", "claus","markus","kristen","anna","tobias","hans"]
print (name_list)
    ##sortere liste
name_list.sort()
print (name_list)
    ##reversere den sorterte listen
name_list.reverse()
print (name_list)

    ##legge til navn i lista med input
new_name_list = input("enter new name: ")
name_list.append(new_name_list)
print (name_list)

name_list.append("trysil")
print (name_list)

"""


### SetTest.py ###

""" ## Define a set
## Set with five favourite foods
favourite_foods = {"chicken","sausage","meat","pizza","burger"}
## Make a second set with friends five favourite fast foods
friend_food = {"pizza","burger","fish","chips","meatballs"}
## add another type of foods to to favourite foods
favourite_foods.add("cola")
print(favourite_foods)
## Determine which foods that you and you friend share as favourites.
print ("Intersection of with food lists: ", favourite_foods.intersection(friend_food)) """


### MyPhonebook.py

""" ## Define a dictionary of five business names and phone numbers. business name should be used as the key.

first_dictionary = ["starbucks":23542354, "pizzabakeren":56435675,"burgerking":23546787,"mcdonalds":23568734]
## Request the name and number of another business from user and add it to the dictionary


## Ask the user to type in the name of a business that is in hte list. Display the result to the user.


## Display the entire dictionary (names and phone numbers)


## Display only the business names (no phone numbers) """


""" Message = "what,is,not,good,I,will,be,you,ok,Noroff,student,Python,a,awesome,pretty,knew,who,would,programmer"
result_one = Message.split(",")
print(result_one)

newmessage = Message.index

print (newmessage[16,15,4,17,6,12,11,18]) """

#Loops
""" 
print("tilstandsløkke")
i = 0
while i <= 10:
    print(i)
    i=i+2

print("telleløkke")
for i in range(0,11,1):
    print(i)
 """

#Funksjon
"""
def f(x):
    return x**2

print (f(1))
"""
# Lister
""" 
tall = []

for i in range (101):
    tall.append(i)
print(tall)
 """
## Create a script called CalculateAreaOfShape.py. 
"""
In the script, create a function called calculate_area_of_shape. 

The function should receive five arguments. 
The first argument should define what shape's area needs to be calculated,
square, cube and circle
The other four arguments should be used to send measurements for 
length, height, width and radius. 

These four arguments should default to the value 0 if not used. 
Your function should calculate the area of at least three different shapes 

In the main section of your script, 
demonstrate the calculation of the area of three shapes. 
Your function calls should make use of named arguments.
"""

""" 
def calculate_area_of_shape(shape, length = 0, height = 0, width = 0, radius = 0):
    if shape == "square" or shape == "cube" or shape == "circle":
        if shape == "square":
            if length > 0 and width > 0:
                print("The square is:", length * width)
            else:
                print("Parametres missing. The square cannot be calculated")
    
        elif shape == "cube":
            if length > 0 and width > 0 and height > 0:
                print("The cube is:", length * width * height)
            else:
                print("Parametres missing. The cube cannot be calculated")

        else:
            if (radius > 0):
                print("The area of the circle is:", 3.14 * radius ** 2)
            else:
                print("Parametres missing. The area of the circle cannot be calculated")
    else:
        print("Shape missing or unknown. Cannot be calculated")
 """
#calculate_area_of_shape("circle")
#calculate_area_of_shape("square",5)
# calculate_area_of_shape("cube",5,5,5)





##  Create a script named splitandjoin.py.

""" #Prompt the user to enter a string of text.
User_text = input("Enter some text:")
print (User_text)

#Ask the user for a character on which to split their text.
bruker_text = input("Which character do you want to split?: ")
print(bruker_text)
#Use this character to split their initial string.
what_split = User_text.split(bruker_text)
print (what_split)
#Request text from the user to use in order to re-combine the string.
#Display the re-combined string to the user.
what_split =User_text(bruker_text)
print(what_split.join) """





## example task school

# Import os to interact with the file system
""" 
import os
# These are the devices that are shown in the task
devices = [["device","type","dateadded","IP Address"],
["computer","pc","1591259971","192.168.100.1"],
["android phone","phone","1591259971","192.168.100.3"],
["samsung phone","phone","1591259971","192.168.100.4"]]

# storing the file name in the variable
file_name = "devices.csv"
# Checking if the "devices.csv" exist or not
if os.path.exists(file_name):
    # append the list to the file
    file = open(file_name, "a")
else:
    # write the file if it does not exist
    file = open(file_name, "w")
# looking at devices list, making a variable where u join the lists in 1 line, then writing the line with a new line
for device in devices:
    line = ",".join(device)
    file.write(line + "\n")
# closing the file
file.close()
  """



"""
from time import *
import random

#Modified version of guessing programe from Xlyme 4.2
#where all metodes are in the same file
#make different files so that there can be imports

# Generate a random number
def randomNumber(maximum):
    tall = random.randint(0, maximum)
    return tall

# The guessinggame program
def guessingNumber():

    # Sets a start time to time how long the game is running
    start = time()
    gameStart = localtime(start)
    
    while True:
        # To break the while-loop and stop the program
        again = input("Press N to quit, or any other key to continue  ")
        if again.lower() == "n":
            break
        
        # We use a try . exsept to hinder bad input from chrashing the program
        try:
            aNumber = int(input("\nGuess a number between 0 and 10  "))
            
            # only numbers between 0 and 10 are valid input 
            if 0 <= aNumber <= 10:
                rightNumber = randomNumber(10)

                if aNumber == rightNumber:
                    print("Congratulation your guess was correct")
                    print("You are a winner\n")

                else:
                    print("Unfortunatly your guess was incorrect")
                    print("your guess was: ", aNumber)
                    print("The right number was:", rightNumber)

            else:
                raise ValueError()   
                print("your guess should be between 1 and 10. Try again\n")
               
        except:
            print("Wrong input. Your guess should be between 1 and 10.\n")
    
    end = time()
    timeDifference = end - start

    print("\nThe Guessing Game ended")
    print("You played the game for", round(timeDifference,), "seconds.")
    print()

guessingNumber()
"""


"""
Create a script called GenerateLetter.py. 
Create a function called generate_letter which is to serve as a generator function. 
The generator should return a letter in the range a to e. 
If the generator returns the letter e, 
it should return the letter a the next time the generator function object is used. 
Demonstrate the use of the generator in the main portion of your script 
by display the letters a to e twice.


def generate_letter():
    while True:
        for letter in "abcde":
            print(letter)
            yield

bokstav = generate_letter()

x = 0
while x < 12:
    next(bokstav)
    x += 1

""" 
##Metricconverter.py

#single metric
#recieve value in inches
# 1 inch = 2,54 cm
""" 
def metric_converter(inches):
    print (inches, "Inches is equal to", inches * 2.54, "centimeters")

metric_converter(10)
 """
 

'''
Create a script called SummingMachine.py. 
In the script, create a function called summing_machine. 
The function should receive no argument. 
It should continuously ask the user to enter a number 
until they enter 's' to stop, 
The values entered must be added together, and the final result 
returned to the calling code. 
Demonstrate the use of the function in the main section of your script.
'''
""" 
def summing_machine():
    
    totalValue = 0

    while True:
        value = input("Type a value: ")

        if value.isdigit():
            value = float(value)
            totalValue += value

        elif value.lower() == "s":
            break

        else:
            print(value, "Cannot be used in calculation\n")
    
    return totalValue

print("Using summing machine")
sum = summing_machine()

print("\nProgrem terminated \nFinal sum:", sum, "\n")
 """

""" 
Create a script called HandleExceptions.py. In the script, create a section of code that requests sales numbers from a user. 
The user should be able to enter as many sales values as they choose to. All sales values should always be entered as float values.
 Each value entered should be added to a list of sales values.
"""
sales = []
while True:
    try:
        sale = float(input("Enter a sale: "))
        sales.append(sale)
    except ValueError:
        print("Invalid input, please enter a number.")
    except:
        print("An error occurred, please try again.")
    choice = input("Do you want to enter another sale? (y/n)")
    if choice.lower() != 'y':
        break

print("Total sales: ", sales)