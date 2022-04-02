import random
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
    finput2()
    input3 = input("That evening, after your nap, you decide to go out for a nice dinner to treat yourself as at work the previous day you got a raise. At the restaurant, you order and everything is very good, although you feel sick after. You assume you just ate something that was a bit off, but it rapidly turns into a stomach churning feeling and you feel like you’re about to vomit your whole body out. You can Call poison control, Vomit in a restaurant tiolet, Scream for help or Hope it's").lower()

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

newMain()
