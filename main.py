import random

from os import system
from time import sleep

def createTree(treeHeight, bombChance = 50):
    spaces = " "   
    spacesString = ""
    readyString = ""
    
    spacesInt = treeHeight
    treeSegment = 1
    printBomb = False
    
    if bombChance > 100 or bombChance < 0:
        print("'bombChance' is greater than 100 or lower than 0")
        exit(1)
    
    for j in range(treeHeight):
        for i in range(spacesInt):
            spacesString+=" "
            
        for i in range(treeSegment):
            if random.randint(0,100) < bombChance:
                readyString += random.choice(["&","#","@","!","~","^"])
                continue
                
            readyString += "*"
            
        print(spacesString,readyString)
        
        spacesInt-=1
        treeSegment+=2
        
        readyString = ""
        spacesString = ""

def main(treeHeight, bombChance = 10, speed = 0.5):
    while True:
        print("\n"*3)
        createTree(treeHeight, bombChance)
        sleep(speed)
        system("clear")
        
main(7, 10, 0.5)
