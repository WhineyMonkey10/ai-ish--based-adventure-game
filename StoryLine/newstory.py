import random
import os
clear = lambda: os.system('clear')
def newMain():
    input1 = input("One day, you’re minding your own business making lunch and you hear shouting from outside. You open your window to see what's going on and you see two people shouting at each other. You can Intervene or Close your window and forget about it: ").lower()
    if(input1 == 'intervene'):
        rnum = random.randint(1, 3)
        if rnum == 1:
            print("You go to intervene and they both stare at you, then stare at eachother and beat you to a pulp")
            return False
        elif rnum == 2:
            print("They thank you, and say “We’re sorry for causing an inconvenience” and leave. You go back home and continue making lunch") #next
        elif rnum == 3:
            print("They start shouting at you")
            return False
    elif input1 == "close your window and forget about it":
        rnum = random.randint(1, 2)
        if rnum == 1:
            print("You eat lunch.")#next
        elif rnum == 2:
            print("You burn your lunch and end up ordering fries.")#next
    clear()
    if finput2() == False:
        return False
    clear()
    input3 = input("That evening, after your nap, you decide to go out for a nice dinner to treat yourself as at work the previous day you got a raise. At the restaurant, you order and everything is very good, although you feel sick after. You assume you just ate something that was a bit off, but it rapidly turns into a stomach churning feeling and you feel like you’re about to vomit your whole body out. You can Call poison control, Vomit in a restaurant tiolet, Scream for help or Hope it's nothing and return home").lower()
    if input3 == "call poison control":
        rnum = random.randint(1, 2)
        if rnum == 1:
            print("Poison control shows up and they cure you")#next
            print("Once home, you decide that the day was very dramatic and that you just want to get to bed and finish off the day. When you’re sleeping, you dream that someone’s out to kill you… You wake up screaming. You check your clock, it’s already 10:45 AM. You’re late to work.")
        else:
            print("Poison control doesn't show up fast enough and you die to severe food poisoning")
            return False
    elif input3 == "vomit in a restaurant toilet":
        print("You vomit into the toilet and survive by a hair")#next
        print("Once home, you decide that the day was very dramatic and that you just want to get to bed and finish off the day. When you’re sleeping, you dream that someone’s out to kill you… You wake up screaming. You check your clock, it’s already 10:45 AM. You’re late to work.")
    elif input3 == "scream for help":
        print("No one comes to your aid, you die from food poisoning.")
        return False
    else:
        print("On your way home, you drop unconscious to the floor, you wake up in a hospital ")
        print("You wake up in a hospital, the doctors tell you that you almost died of food poisoning, but you can go home now. You go home, but realize that it’s already 10:45 AM. You’re late to work.")
    clear()
    input4 = input("You realize that you have to go to work no matter what, now you finally have an easy choice. \n You can Take the bus a94 to your work. Take the train 6WA to your work or Walk to your job").lower()
    if input4 == "take the bus a94 to your work":
        print("Once you get on the bus, the driver says that it will be making a detour back to the main bus station because of some minor issues. You, realizing that this would making you late, decide to hop on the train 6WA. You arrive an hour late to work. ")#next
    elif input4 == "take the train 6wa to your work":
        rnum = random.randint(1, 3)
        if rnum == 1:
            print("The train makes it to your office, but you’re 50 minutes late.")#next
        elif rnum == 2:
            print("The train makes a 10 minute stop at the station right before your station to remove someone who is disturbing the driver. You’re an hour late.")#next
        else:
            print("The train skips a stop before yours, you’re late, but only 45 minutes late.")#next
    elif input4 == "walk to your job":
        print("You walk to work, on your way there you see nature. Although, you’re one and a half hours late.")
    print("This is the end so far.")
    input("Press enter to exit")

def finput2():
    input2 = input("After lunch, you’re feeling a bit tired and decide to take a nap, in the middle of your nap you hear something like a blender turning on and question why it’s so loud. You walk downstairs and see that your blender is running. Although, you’re 100 percent sure that you locked your doors. You can Call homeland security, Go back to bed or Search your house (note that with everything you turn off the blender): ").lower()
    if input2 == "call homeland security":
        print("Homeland security tries to sell you security cameras for your house, but you don’t feel comfortable with that, so you politely decline.") #next
    elif input2 == "go back to bed":
        rnum = random.randint(1, 2)
        if rnum == 1:
            print("You hear more blending noises an hour later")#repeat
            finput2()
        else:
            print("You sleep well ")#next
    elif input2 == "search your house":
        rnum = random.randint(1, 2)
        if rnum == 1:
            print("You search your house unsuccessfully and return back to sleep ") #next
        else:
            print("You enter your basement but trip on the stairs and break your spine.")
            return False