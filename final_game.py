import os
import time
werewolf_clues=0
lockbox=False
car_key=False
dining_room=False
study=False
bedroom_nursey=False 
garage=False
painting_door=False
safe_lock=False
painting_counter=0
silver=False
laptop=False
basement_choice=False
player_dead=False
cultist="ALIVE"
restart=""
bed_choise=False
living_room=False
ending_choice=False

def start_game(): 
 time.sleep(3)
print("created by/Michael/Geraldine")
time.sleep(3)
print("""                  
 / _|     | | |                                                              
| |_ _   _| | |  _ __ ___   ___   ___  _ __     ___ ___  ___ __ _ _ __   ___ 
|  _| | | | | | | '_ ` _ \ / _ \ / _ \| '_ \   / _ / __|/ __/ _` | '_ \ / _ \
| | | |_| | | | | | | | | | (_) | (_) | | | | |  __\__ | (_| (_| | |_) |  __/
|_|  \__,_|_|_| |_| |_| |_|\___/ \___/|_| |_|  \___|___/\___\__,_| .__/ \___|
                                                                 | |         
""")
print(""" 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@'~~~     ~~~`@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@'                     `@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@'                           `@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@'                               `@@@@@@@@@@@@@@@
@@@@@@@@@@@'                                   `@@@@@@@@@@@@@
@@@@@@@@@@'                                     `@@@@@@@@@@@@
@@@@@@@@@'                                       `@@@@@@@@@@@
@@@@@@@@@                                         @@@@@@@@@@@
@@@@@@@@'                      n,                 `@@@@@@@@@@
@@@@@@@@                     _/ | _                @@@@@@@@@@
@@@@@@@@                    /'  `'/                @@@@@@@@@@
@@@@@@@@a                 <~    .'                a@@@@@@@@@@
@@@@@@@@@                 .'    |                 @@@@@@@@@@@
@@@@@@@@@a              _/      |                a@@@@@@@@@@@
@@@@@@@@@@a           _/      `.`.              a@@@@@@@@@@@@
@@@@@@@@@@@a     ____/ '   \__ | |______       a@@@@@@@@@@@@@
@@@@@@@@@@@@@a__/___/      /__\ \ \     \___.a@@@@@@@@@@@@@@@
@@@@@@@@@@@@@/  (___.'\_______)\_|_|        \@@@@@@@@@@@@@@@@
@@@@@@@@@@@@|\________         hjk.          ~~~~~\@@@@@@@@@@  """) 
time.sleep(3)
response = input("Ready to play? [Y/N] ")
if response.upper() == "Y" or response.upper() == "Yes":
    time.sleep(2)
    print("lets go.")
elif response.upper() =="N"  or response.upper()=="NO": 
    print("Bye")
    exit()
else:("Please try again")
import sys
import time
def print_slow(str):
    for char in str:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
print_slow("You have awoken in a dark room,")
print_slow(" confused you feel  around and find your phone in your pocket,")
print_slow(" Looking at the screen you unlock it by entering your name\n")
#def what_name():
#    global name
#    name = input("what is your name? ")
#    time.sleep(1)
#    print(f"Hello {name}, nice to meet you")
#    time.sleep(2)
response = input("type name: ") 
print("""
__________$$$$$$$$$$
_________$_________$$
_________$_$$$$$$$_$$
_________$_$_____$_$$
_________$_$_____$_$$
_________$_$_____$_$$
_________$_$_____$_$$
_________$_$$$$$$$_$$
_________$_________$$
__________$$$$$$$$$$
_________$_________$$
________$_1__2__3_$$$
_______$_4__5__6_$$$
______$_7__8__9_$$$
_____$_*__0__#_$$$
____$_________$$$
_____$$$$$$$$$$$
______$$$$$$$$$
""")
time.sleep(0.2)
print_slow("looking around using the light from the phone you see a light switch on the wall a torch on a table and light coming through a door with voices from the other side")
time.sleep(1)
while basement_choice==False:
    response = input("turn on the lightswitch? [Y/N]")
    if response.upper() == "Y" or response.upper() == "YES":
        time.sleep(3)
        print("A loud voice suddenly erupts to your right coming from the door with the light.")
        print("You quickly run and hide inside a wardrobe as loud footsteps get closer.")
        print_slow("Somthing has entered the room.")
        print_slow("Trembling inside you hear a *click* and realize that you have been locked inside.")
        print("Terrified you feel around the wardrobe feeling silks and furs likely very expensive clothing as somthing runs across your feet")
        print('''
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /
                          (((-'    __//
                                 (((-'
    ''')
        print("A huge Rat is biting you, as you kick at it, you hear the sound of somthing dropping on the floor, Looking down you find a key. ")
        print("picking up the key you stab it hard into the rat killing it")
        print_slow("wiping it off on your sleeve you use it to unlock the door")
        print_slow("creeping outside you spot a different door ")
        print_slow("You move towards it slowly and begin to open the door and step outside. You come across a locked door the door has an inscription on it:\nThrough the forest the red hood wanders. The chimney of the old ladies house pours out a welcoming smoke. When the door opens the wolf attacks.")
        time.sleep(0.1)
        basement_choice = True
    elif response.upper() == "N"or response.upper == "NO":
        time.sleep(1)
        print("you instead pick up the torch")
        time.sleep(0.2)
        print_slow("picking up the torch you shine it around the room, you see a door.")
        print_slow("you slowly open the door")
        print_slow("creeping through the door, you find yourself in a hallway")
        print("""
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
     """)     
        print_slow("As you enter the hallway you come across a locked door the door has an inscription on it:\nThrough the forest the red hood wanders. The chimney of the old ladies house pours out a welcoming smoke. When the door opens the wolf attacks.")
        
        time.sleep(0.1)
        basement_choice = True
    else:
        print("That isn't an accepted response")
while painting_door==False and painting_counter<3:
    response=input("""Put the paintings in order
1) Red Hood
2) Howling Wolf
3) Cottage with the chimnet
4) Tranquil Forest
:""")
    if response.upper()=="4132" or response.upper()=="4 1 3 2":
        print("You've unlocked the door")
        painting_door=True
    elif response.upper()!="4132" and response.upper()!="4 1 3 2" and painting_counter<2:
        print("No that order is wrong you fool try again")
        painting_counter += 1
    else:
        print("You've triggered a trap you fall and die on a pit of spikes")
        painting_counter += 1
        player_dead=True
        restart = input('do you want to restart (1) or continue and pretend you got that puzzle (2) ?')
        if restart.upper()=="1":
            exit()
        elif restart.upper() == "2":
            continue
        else:
            print("That isn't an option")

print_slow("You ascend the stairs and find yourself in some kind of entry way to a large house just in front of you is a set of double doors that appear to be the main entrance but upon further inspection they are locked tight. you then move to the only other door you see. ")
print_slow("Upon opening the door the smell of hits you first the smell of rot.") 
print_slow("Rotten food, flies and maggots litter the table and fill the room with smell and noise.")
print_slow("You finally notice in the opposite corner of the room is a safe.")
print_slow("You approach the safe it has writings just above the door")
time.sleep(1)
while safe_lock==False:
    print("""Above the safe there is a note that reads:
Ax3=9
A+W=12
W-A=L
O=A-1
F=O+L
and on the safe it reads W-O-L-F the note must be a clue to the code!""")
    response=input("The code must be:")
    if response.upper()=="9268" or response.upper()=="9-2-6-8" or response.upper()=="9 2 6 8":
        print("Yes the safe is open you find some bright polished silverware inside you decide to take a a cup a knife and a spoon in your bag")
        safe_lock=True
        silver=True
    else:
        print("That code didn't seem to work look at the note again")
print("Within the safe you find beautiful pieces of silverware you decide to take them and head back to the foyer")
silver=True
time.sleep(1)
print_slow("After exiting the putrid dining hall you notice a door that you didnt see before going through the door you come upon a comfotable study the warmth from the once lit fireplace putting you at ease")
print_slow("On a desk to the left of you there is a laptop to your right a bookcase directly before you the warm fireplace and its quickly cooling ashes. ")
print_slow("The laptop screen lights up much to your surprise but blast! it needs a password")
print_slow("The bookcase seemingly lacks anything of of intrest however, you do notice that there seens to be a considerable gap and some diaries presumably of the owner of the house? someone named Rossa.")
print_slow("Looking at the fireplace more closely you notice that there was paper used for kindling.Rooting through the ashers you notice that not all of the pages are completely burned and on one you can make out P_s_wo_d:L__n_t_r__y")
while laptop==False:
    print("That note must be the password to the laptop")
    response=input("The password must be: ")
    if response.upper()=="LYCANTHROPY":
        print("Success the laptop is open and it's open to a document about cures for werewolves but it isn't complete it just says something about needing blood from the hunter?")
        laptop=True
        werewolf_clues += 1
    else:
     print("No that's the wrong password think again")
     print("You leave the study")
print_slow("An interesting discovery to be sure but you need to know more. You exit the study and again notice another door that you're sure wasn't there before despite any hesitation you know you need to move and escape this horrifying place and so move to open the door")
while garage==False:
    response=input("""You quietly open the door and then see a figure stood next to a car what do you do?
    1) Attack them from behind the bastard has it coming
    2) Sneak in and listen to what they say it might be worthwhile
    [1/2]
    """)
    if response.upper()== "1":
        print_slow("You go to grab the hooded man from behind but before you do you hear him mumbling something about wanting to get some keys from upstairs and go for a joy ride something about them being in a bedroom drawer and decide to instead find that key")
        garage=True
    elif response.upper()== "2":
        print_slow("The hooded man is mumbling something about wanting to get some keys from upstairs and go for a joy ride something about them being in a bedroom drawer")
        garage=True
    else:
        print("That wasn't an option")
print_slow("Having finished what you needed to do in the garage you once again exit the room and come to find a staircase where you are adamant there wasn't a staircase before reluctantly however you know that you must ascend these stairs if you are ever to escape")
print_slow("Coming to the top of the stairs you are met with 2 doors you move through the first door and come into an immaculate bedroom beautifully furnished with expensive finery you find yourself drawn to the bed")
while bed_choise==False:
    response=input("""The bed seems to be calling to you enticing you to sleep you're body aches and you feel the exhuastion from your ordeal weighing on you do you
    1) Get in the bed and try to sleep
    2) resist the urge and press on
    [1/2]: 
    """)
    if response.upper()=="1":
        print("You lay down on the bed and quickly drift to sleep you do not wake up again")
        player_dead=True
        while player_dead==True:
            restart = input('do you want to restart Y/N?')
            if restart.upper() == 'N' or restart.upper()=="No":
                exit()
            elif restart == 'Y':
                start_game
    elif response.upper()=="2":
        print("You struggle to do it but you manage to resist the urge to lie down in the bed")
        bed_choise=True
    else:
        print("That was not an option")
print_slow("next to the bed is a set of drawers Inside the set of drawers there is a lockbox shaking the box there is something inside maybe a set of keys? but you need a key to get it open")
print_slow("You notice that there is a door off to the side and after investigating the drawers in the room and only finding expensive womens clothing you move to the door")
print_slow("The next room is a nursery with a crib in one corner and various baby supplies along one wall")
print_slow("First checking amongst the baby supplies you find nothing of any real interest there are bottles and nappies and all sorts of baby foods")
print_slow("You go to the crib and notice the dark dried blood that has soaked through you try not to think too hard about what that might mean")
print_slow(" Tentatively you move away the sheets and find hidden beneath them a childrens story book in fact your mothers favourite to read to you when you were a child: 'little red riding hood' cautiously you open the book and a piece of paper drops out ")
print_slow("you retrieve the paper and read: 'Blood and Silver it only needs blood and silver' the writing is scrawled as if written in a flurry but you realise that this must be referring to the supposed werewolf cure! ")
print_slow("You make your way back through to the landing and are once again met with a new door checking behind yourself you see that the door you just came through is now gone ")
print_slow("now more determined than ever to escape you move to the next door ")
print_slow("Upon opening the door you are greeted with a room that appears to be something like a living room oddly homely in stark contrast to the rest of the dilapidated mansion ")
while living_room==False:
    response=input("""You move further into the room until you notice a huge wolf lying down on the sofa taken aback you nearly awaken but catch yourself you notice that the wolf has something around its neck... A KEY!
    do you
    1) Kill the wolf in its sleep so you can take the key freely?
    2) Sneak over and take the key from around the wolfs neck after all it seems to be in a very deep sleep
    [1/2]
    """)
    if response.upper()=="1":
        print_slow("You stab the wolf and its eyes shoot open it eventually focuses on you and hate fills its gaze it lunges at you going for your neck!")
        player_dead=True
        restart = input('do you want to restart (1) or continue and pretend you got that puzzle (2) ?')
        if restart.upper()=="1":
            exit()
        elif restart.upper() == "2":
            continue
        else:
            print("That isn't an option")
    elif response.upper()=="2":
        print_slow("""You decide to instead simply sneak over and try and take the key without being noticed the wolf does after all appear to be in a deep slumber...
        
        Success! you manage to get the key from around the wolfs neck""")
        living_room=True
    else:
        print("That wasn't an option")
print_slow("The key fits in the lockbox and once open reveals a set of car keys!")
print_slow("You have the all you need to escape with this car key but then the question remains what of the werewolf cure? If it works you not only save yourself but likely countless others")
while ending_choice==False:
    response=input("""Do you:
    1) Try to make the cure?
    2) Just escape in the car
    [1/2]""")
    if response.upper()=="1":
        print_slow("You slice your hand with the silver knife from the safe and allow the blood to fill the silver cup you obtained from the safe the crimson liquid pooling inside you take the knife and scrape as much silver into the cup as you can and mix it up but now how to administer the cure?")
        response=input("""Do you:
        1) Throw the cup at the werewolf?
        2) Try and put the concoction in something the werewolf will eat?
        3) Give up and escape in the car?
        """)
        if response.upper()=="1":
            print_slow("You make your way back down into the basement of the old mansion careful not to make too much of a sound you come to the door where you first awoke and quietly open the door before you you see what can only be described as an evil occult ritual in the middle of the room lies a dais with one of the cultists lied upon it cut open and dead at the opposite door there stands the wolf you now know to be called Rossa you move over to her and fling the silver cup filled with blood at her this accomplishes nothing but making her notice you and be extremely angry she lunges towards you and the world goes dark")
            ending_choice=True
        elif response.upper()=="2":
            print_slow("You make your way back down into the basement of the old mansion careful not to make too much of a sound you come to the door where you first awoke and quietly open the door before you you see what can only be described as an evil occult ritual in the middle of the room lies a dais with one of the cultists lied upon it cut open and dead you move towards them and pour the potion over the body you retreat to the entrance and watch as the wolf that you now know is called Rossa makes her way to the dead man and begins to devour what is left of him until suddenly she begins to convulse shaking and wretching and writhing on the floor this seems to go on for some time until she stops and a little girl no more than 10 bursts from the stomach of the beast. You have cured the girl of her curse. but now what? The End")
            ending_choice=True
        elif response.upper()=="3":
            print_slow("""You make your way down the stairs and come to the door to the garage the cultist that was there before miraculously has moved on you get into the car put the key in the ignition and feel the engine roar to life you get the car going and break through the old wooden garage door splinting as the car rams through the mansion disappears into the night in the rear-view mirror is it possible have you really lived through the nightmare and what of those that took you will they follow you?
            """)
            ending_choice=True
        else:
            print("That wasn't an option")
    elif response.upper()=="2":
        print_slow("""You make your way down the stairs and come to the door to the garage the cultist that was there before miraculously has moved on you get into the car put the key in the ignition and feel the engine roar to life you get the car going and break through the old wooden garage door splinting as the car rams through the mansion disappears into the night in the rear-view mirror is it possible have you really lived through the nightmare and what of those that took you will they follow you?
            """)
        ending_choice=True
    else:
        print("That wasn't an option")

start_game()