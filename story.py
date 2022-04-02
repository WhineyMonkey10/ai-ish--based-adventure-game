def main():
    ready = input("Are you ready? Please type Yes If you are. ").lower
    if ready == ("Yes"):
        bedroomtodownstairs = input("One night, you are chilling in your bedroom when you hear a strange noise from downstairs, you wonder if you should go. Yes Or No? ").lower
        if bedroomtodownstairs == ("Yes"):
            hidedownstairs1 = input("You creep downstairs making sure that that you don't make any noise on the steps. And suddenly you see movement. What do you do? Hide or Continue looking? ").lower
        if hidedownstairs1 == ("Hide"):
          lookorhideclosethiding1 = input("You decide to hide in the closet and go all the way to the back to hide behind a thick layer of coats. You hear footsteps going towards your direction, you hope that they are just walking to the kitchen as it is right next to you. But you arent sure. Do you Continue hiding or do you try to Take a look? ").lower
          if lookorhideclosethiding1 == ("Continue hiding"):
            escapetownpoliceorcamp = input("You continue hiding but get impatient, so you silently walk out of the closet, and you see a strange figure in you kitchen looking inside your fridge. You decide that this is a perfect time to escape. So you quickly escape through the front door and run until you get to the town. What do you do here? Stay the night or Go to the police? ").lower
            if escapetownpoliceorcamp == ("Go to the police"):
              policeaccuiredsleepoutside = input("You go to the police station and explain exactly what happened. The listen to your full story and proceed to tell you that they have had many reports all about the same sort of person and they all say that the person snuck in at almost 10:58 PM. The police say that they will go to you house the next day. So they say that you can stay the night because its very cold outside. Do you Stay the night or sleep outside? ").lower
              if policeaccuiredsleepoutside == ("Stay the night"):
                stayorrunending = input("You stay the night at the police station, they let you sleep there. You thank them for being so kind and you go to bed. The next morning they wake you up and say, Alrigh, time to go look at your house. So you get dressed grab something to eat and go with them to your house. They ask you many questions, you answer all of them. Then they say that something is strange, they creep upstairs and see a strange figure standing in YOUR room!! They capture them, put them in handcuffs and say that they hear a ticking noise to you. Do you stay inside the house or Run? ").lower
                if stayorrunending == ("Run"):
                  print("You run as fast as you possibly can with the police and the strange figure right infront of you. As soon as everyone gets out of the house... it DISSAPEARS!! The police don't understand what happened and send the strange figure to a ant-magic jail... Part 2 coming soon")
                else:
                    print("The house dissapears into a strange realm with only darkness and the house floating around in it. You endup starving to death with the strange figure and the cops with you. Try again.")
              else:
                  print("You try to sleep outside for the night, but because you live in a house with heating and are not used to cold climates you get a shock from staying in the same position for so long in the cold. You end up dying during the night.")
            else:
                print("You try to sleep outside for the night, but because you live in a house with heating and are not used to cold climates you get a shock from staying in the same position for so long in the cold. You end up dying during the night.")
          else: 
              print("You decide to take a look, all of a sudden you get slapped so hard on your face you go flying to outerspace and sufficate there. Try again.")
    
        else:
            print("Suddenly a hot pot of boiling water falls on your head, and you die. Try again.")
    
    

    else:
        print("Suddenly the roof falls on your head. And you die, try again.")