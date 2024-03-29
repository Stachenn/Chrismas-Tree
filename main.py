# Make by Stanislaw Janowski (Stachenn) 06.01.2024
# Import Libraries

from random import randint, choice

from os import system, name
from time import sleep

BLACK = "30"
RED = "31" 
GREEN = "32"
YELLOW = "33"
BLUE = "34"
MAGNETA = "35"
CYAN = "36"
WHITE = "37"
GRAY = "90"
BRIGHTRED = "91"
BRIGHTGREEN = "92"
BRIGHTYELLOW = "93", 
BRIGHTBLUE = "94" 
BRIGHTMAGNETA = "95"
BRIGHTCYAN = "96"
BRIGHTWHITE = "97"

COLORS = ["30", "31", "32", "33", "34", "35", "36", "37", "90", "91", "92", "93", "94", "95", "96", "97"]

# Declare function that creating tree
def createTree(treeHeight, decorationChance = 50):
    # Declare varibles
    spaces = " "   
    spacesString = ""
    readyString = ""
    
    spacesInt = treeHeight
    treeSegment = 1

    # Checking that procent is not greter than 100 or lower than 0
    # If yes then exit with error
        
    if decorationChance > 100 or decorationChance < 0:
        print("'bombChance' is greater than 100 or lower than 0")
        exit(1)

    # Creating loop that printing tree using varible named treeHeight that printing tree from segments
    for j in range(treeHeight):
        # Creating another loop in loop that adding saces to string
        for i in range(spacesInt):
            spacesString+=" "

        # And another loop that adding chrismas decoration or normal tree
        for i in range(treeSegment):
            # Checking is chance greater than random chance            
            if randint(0,100) < decorationChance:
                # Adding random char from list to ready string           
                readyString += f"\033[{choice(COLORS)}m{choice(['&','#','@','!','~','^'])}\033[m"
                continue

            # Adding normal segment to ready string
            readyString += "*"
            
        # Printing spaces and ready string
        print(spacesString,readyString)

        # Addition and subtraction from treeSegment and spaceInt
        spacesInt-=1
        treeSegment+=2

        # Restarting string Varible
        readyString = ""
        spacesString = ""

# Declare function that running program
def main(treeHeight, decorationChance = 10, speed = 0.5):
    while True:
        # Creating 3 spaces
        print("\n"*3)
        # Creating tree
        createTree(treeHeight, decorationChance)
        # Wait 'speed' second
        sleep(speed)

        # Checking os and clearing screen
        if name == "posix":
            system("clear")
        if name == "nt":
            system("cls")
                
# Running program   
main(50, 30, 0.25)
