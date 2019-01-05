# cd desktop
# python wizards.py

# save feature:
# with open('savefile', 'w') as f:
#   pickle.dump(data, f)

# load feature:
# with open('savefile') as f:
#   data = pickle.load(f)

from pygame import mixer
import random
import os
import time
import sys
import pickle

mageLvl = 1
health = 100
gold = 0
name = "n"

def exit():
    sys.exit()


def refreshScreen():
    clear = lambda: os.system('cls')
    clear()

def musicTurtle():
    mixer.init()
    mixer.music.load('C:/Users/TimothyPC/Downloads/sansmusic.mp3')
    mixer.music.play()

def musicMain():
    mixer.init()
    mixer.music.load('C:/Users/TimothyPC/Downloads/wow.mp3')
    mixer.music.play()

def titleScreen():
    print("  _ ___           _                  _    ___  _ ")
    print(" | |__ \         (_)                | |  |__ \| |")
    print(" | |  ) |_      ___ ______ _ _ __ __| |___  ) | |")
    print(" | | / /\ \ /\ / / |_  / _` | '__/ _` / __|/ /| |")
    print(" |_||_|  \ V  V /| |/ / (_| | | | (_| \__ \_| |_|")
    print(" (_)(_)   \_/\_/ |_/___\__,_|_|  \__,_|___(_) (_)")
    print("                                                 ")
    startOrExit = input("Start or exit? (y/n) ")
    if(startOrExit == "y"):
        refreshScreen()
        loading1()
    else:
        exit()
        refreshScreen()

def lvl1():
    print(turtle1)


def character():
    print("              _,._       ")
    print("  .||,       /_ _\\      ")
    print(" \.`',/      |'L'| |     ")
    print(" = ,. =      | -,| L     ")
    print(" / || \    ,-'\"/,'`.    ")
    print("   ||     ,'   `,,. `.   ")
    print("   ,|____,' , ,;' \| |   ")
    print("  (3|\    _/|/'   _| |   ")
    print("   ||/,-''  | >-'' _,\\  ")
    print("   ||'      ==\ ,-'  ,'  ")
    print("   ||       |  V \ ,|    ")
    print("   ||       |    |` |    ")
    print("   ||       |    |   \   ")
    print("   ||       |    \    \  ")
    print("   ||       |     |    \ ")
    print("   ||       |      \_,-' ")
    print("   ||       |___,,--')_\ ")
    print("   ||         |_|   ccc/ ")
    print("   ||        ccc/        ")
    print("   ||                    ")

turtle1 = (r'''                                     ___-------___
                                 _-~~             ~~-_
                             _-~                    /~-_
          /^\__/^\          /~  \                   /    \
         /| O ||O |       /     \_______________/          \
        | |___||__|      /       /                \          \
        |          \    /      /                    \          \
        |   (_______) /______/                        \_________ \
        |         / /         \                      /             \
         \         \^\\         \                  /                 \     /
          \         ||           \______________/      _-_          //\__//
           \       ||------_-~~-_ ------------- \ --/~   ~\        || __/)
            ~-----||====/~      |==================|       |/~~~~~
             (_(__/  ./       /                   \_\      \.
                       (_(___/                       \_____)_)''')

turtle2 = (r'''


                                                    ___-------___
                                 _-~~             ~~-_
                             _-~                    /~-_
          /^\__/^\          /~  \                   /    \
         / /\  /\|       /     \_______________/          \
        | /  \/  \\      /       /                \          \
        |          \    /      /                    \          \
        |   (_______) /______/                        \_________ \
        |         / /         \                      /             \
         \         \^\\         \                  /                 \     /
          \         ||           \______________/      _-_          //\__//
           \       ||------_-~~-_ ------------- \ --/~   ~\        || __/)
            ~-----||====/~      |==================|       |/~~~~~
             (_(__/  ./       /                   \_\      \.
                       (_(___/                       \_____)_)''')

turtleDialogue = ["A curious little turtle saw you. It is staring into your soul...",
                  "Hello! My name is Ted the turtle! My task is to teach you the game mechanics and give you tips!",
                  "Oh no its an enemy! Attack it by pressing 1. Later you will have access to other attacks and spells!",
                  "Hurray! You have defeated the monster!", "You can always save later!"]

def lvl1():
    musicTurtle()
    for char in turtleDialogue[1]:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def charName():
    name = input("Enter your name: ")
    print("Hello there", name, "lvl", mageLvl,"young mage!")
    time.sleep(2)
    refreshScreen()

data = {"Health": health, "Gold": gold, "Name": name}

def after1():
    print(turtle1)
    time.sleep(5)
    refreshScreen()
    lvl1()

def loading1():
    for i in range(2):
        print("You are a young wizard with a passion towards your fathers craft... You want to become the best and beat everyone! Survive every tournament!")
        print("Loading.")
        time.sleep(0.7)
        print("Loading..")
        time.sleep(0.7)
        print("Loading...")
        refreshScreen()
    readyNo = input("Are you ready? (y/n): ")
    if(readyNo == "y" or "yes"):
        refreshScreen()
        charName()

name = "no one"

musicMain()

titleScreen()
mixer.music.stop()
after1()
