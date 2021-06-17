#'print("hello world")
#String data type
#Represents text - "in quotes"

#print(5)
#Integer - whole number

#print(5.1)
#Floating point - decimal number

#print(True)
#print(False)
#Boolean - True or False



#print("I didn't just become a little bit of a slag, I became a total slag")
#print(len("I didn't just become a little bit of a slag, I became a total slag"))
#print(len("2001 A Space Odyssey"))
#len gives the total amount of characters within a string



#print("2001 A Space Odyssey"[0])
#Start counting from 0
#index position
#Start counting from 0 
#Or take away 1 from the real number - so 1st character is 1 - 1 = 0



# Dot Notation - Connect data to the method using a dot
#print("Hello".upper())
#.upper() makes a string upper-case
#.lower() makes a string lower-case
#Others include .capatalize(), .count(), .find(), .replace(), .strip()



#Libraries
#print is an in-built library
import random
#imported libraries should be at the top to hopefully prevent any errors

#'print(random.random())
#The above will print a random number using the random library and the random method
#This will print a floating point number between 0 and 1

#print(random.uniform(1,11))
#The above will print a random number between 1 and 10
#This will print a number between the two numbers that are defined

#print(random.randint(1,10))
#This generates a integer between the values provided

#from random import random, randint, uniform
#it is possible to import specific methods



#Activity 1
#print("   |   |   \n_ _|_ _|_ _\n   |   |   \n_ _|_ _|_ _\n   |   |   \n   |   |   ")
#A Grid for noughts and crosses



#Activity 2
#print("i'm yelling".upper())
#The .upper() method alters a string so that all the letter characters are upper-case

#print("I'M WHISPERING".lower())
#The .lower() method alters a string so that all the letter characters are lower-case

#print("i'm talking normally".capitalize())
#The .capitalize method alters a string by capitalizing the first character but only if it is a letter
#print("41 thousand years".capitalize())
#Here the capatilize method doesn't alter the string as the first character isn't a letter
#It is important to remember that it capitalises the first character (if it's a letter) and makes all other letters lower-case

#flowers = ["Rose", "Daisy", "Tulip", "Chrysanthemum", "Violet", "Daffodil"]
#x=flowers.count("Rose")
#print(x)
#The count method counts the number of times the string/integer/ data point appears in a list
#Can also be used in a regular string to find how many times the substring appears within the main string for example
#print("Hello darkness my old friend".count("e"))

#script="To be, or not to be, that is the question, Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles And by opposing end them."
#line=script.find("trouble")
#print(line)
#The find method finds the first instance of the given string/integer requested and its index position
#If not found then -1 is printed for example
#wrong=script.find("Bonanza")
#print(wrong)
#As there was no instance of the string Bonanza -1 was returned
#It is possible to search for a specific instance in a range this is done as below
#finder=script.find("the", 20, 100)
#print(finder)

#The replace method replaces a specified value with a new preferred value
#loveletter="Shall I compare thee to a summers day"
#print(loveletter)
#hateletter=loveletter.replace("Shall I", "I wouldn't")
#print(hateletter)
#All instances will be replaced as below
#shanty="What do we do with a drunken sailor?"
#reply=shanty.replace("do", "don't")
#print(shanty)
#print(reply)
#As below a the number of instances to be replaced can be specified
#correction=shanty.replace("do", "don't", 1)
#print(correction)

#the strip method removes unneeded spaces at the beginning and end of a given string example
#print("      Hello     ".strip())

#print("when using print to create a new line simply combine \ and n like so\n/n doesn't work")

#favouritethings="Raindrops on roses, whiskers on kittens, Bright copper kettles, warm woolen mittens, Brown paper packages tied up with strings".split(", ")
#print(favouritethings)