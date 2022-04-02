# Imports & Starting Code
import random
import sys
sys.path.insert(1, '/StoryLine/story.py')
from StoryLine.newstory import *
import os
clear = lambda: os.system('clear')
clear()

# Execution


if newMain() == False:
    input("You lost the game. \nPress enter to exit")

# Credits: https://github.com/WhineyMonkey10 & https://github.com/hogefoot
# Project Page: https://github.com/WhineyMonkey10/ai-ish--based-adventure-game
