# Code for going into the game project

#import time
#import random

#hp=200
#atk=25
#pdef=10
#spd=10

#edef=15

#damage= int(((atk**2)-(int((edef/2))**3))/5)
#print(damage)


#print('''
#  ad8888888888ba
# dP'         `"8b,
# 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
# 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
# 8  8   8              """        """      ""    8b
# 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
# 8  `"""'       ,d8""
# Yb,         ,ad8"
#  "Y8888888888P"''')


#print('''
#               _     __,..---""-._                 ';-,
#        ,    _/_),-"`             '-.                `\\
#       \|.-"`    -_)                 '.                ||
#       /`   a   ,                      \              .'/
#       '.___,__/                 .-'    \_        _.-'.'
#          |\  \      \         /`        _`""""""`_.-'
#             _/;--._, >        |   --.__/ `""""""`
#           (((-'  __//`'-......-;\      )
#                (((-'       __//  '--. /
#                          (((-'    __//
#                                 (((-'
#''')
werewolf_clues=0
lockbox=False
car_key=False
dining_room=False
study=False
bedroom_nursery=False
living_room=False
garage=False
painting_door=False
safe_lock=False
painting_counter=0
silver=False
laptop=False

#print("As you enter the hallway you come across a locked door.")
#print("taking a closer look you notice an inscripton on the door. It reads Through the forest the red hood wanders. The chimney of the old ladies house pours out a welcoming smoke. When the door opens the wolf attacks.")
#print("scanning the hallway you notice some paintings that seem to correspond to the inscription on the door. There are four paintings each depicting a unique scene the first shows a red hooded figure the second a wolf howling at the moon, the third a pleasant countryside cottage with smoke billowing out of the chimney, the final painting shows a tranquil forest")
#while painting_door==False and painting_counter<3:
#    response=input("""Put the paintings in order
#1) Red Hood
#2) Howling Wolf
#3) Cottage with the chimnet
#4) Tranquil Forest
#:""")
#    if response.upper()=="4132" or response.upper()=="4 1 3 2":
#        print("You've unlocked the door")
#        painting_door=True
#    elif response.upper()!="4132" and response.upper()!="4 1 3 2" and painting_counter<2:
#        print("No that order is wrong you fool try again")
#        painting_counter += 1
#    else:
#        print("You've triggered a trap you fall and die on a pit of spikes")
#        painting_counter += 1

#while safe_lock==False:
#    print("""Above the safe there is a note that reads:
#Ax3=9
#A+W=12
#W-A=L
#O=A-1
#F=O+L
#and on the safe it reads W-O-L-F the note must be a clue to the code!""")
#    response=input("The code must be:")
#    if response.upper()=="9268" or response.upper()=="9-2-6-8" or response.upper()=="9 2 6 8":
#        print("Yes the safe is open you find some bright polished silverware inside you decide to take a a cup a knife and a spoon in your bag")
#        safe_lock=True
#        silver=True
#    else:
#        print("That code didn't seem to work look at the note again")


#print("Rooting through the ashes you notice that not all of the pages are completely burned and on one you can make out: pa__wo_d: L___n_t_r__y")
while laptop==False:
    print("That note must be the password to the laptop")
    response=input("The password must be: ")
    if response.upper()=="LYCANTHROPY":
        print("Success the laptop is open and it's open to a document about cures for werewolves but it isn't complete it just says something about needing blood from the hunter?")
        laptop=True
        werewolf_clues += 1
    else:
        print("No that's the wrong password think again")
