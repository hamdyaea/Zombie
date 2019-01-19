# Developer Hamdy Abou El Anein
# This game is text game in a world full of zombies

from sys import exit

zombie_alive = True
Big_zombie_alive = True
gun = False


def room_1():
    print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
    print("Welcome to the Zombie text game")
    print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
    print("After a virus created in the laboratory has been released by accident the world is now full of zombies.")
    print("You are in a big room with blood covered walls. You have a gun in your bag.")
    print("It's really dark and all you can see is three doors.")
    print("They lead east, north and west. What do you do?")
    print("Enter : east, north or west")
    choice = input("> ");

    if "west" in choice:
        room_2()
    elif "north" in choice:
        room_4()
    elif "east" in choice:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("""You carefully go through the narrow passage heading
east. After walking for three minutes, you see that
it ends with a solid wall. You turn around to get back
but you find yourself facing another wall. Somewhat,
you have trapped yourself. Without water nor food, you
die some days later. After that, you wake up as a zombie.""")
        game_over()
    else:
        room_1()

def room_2():
    print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
    print ("This room has a really low ceiling and you must crouch to walk.")
    print ("You see a passage leading west and a passage leading north.")
    print ("On the far end of the first one, you can see a bright light.")
    print ("From the second one, a really bad smell emanates.")
    print ("The passage to the east leads to the first room.")
    print ("What do you do?")
    print("Enter : east, north or west")

    choice = input("> ");

    if "west" in choice:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("""You follow the bright path. As you walk, there are 
more and more noise.
Suddenly the floor fall under your
feet and, as you fall in a hole with a lot of zombies, you understand
where the noise came from. You die screaming in pain then you become a zombie.""")
        game_over()
    elif "north" in choice:
        room_3()
    elif "east" in choice:
        room_1()
    else:
        room_2()

def room_3():

    global zombie_alive
    global gun

    if zombie_alive:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("As you walk into the room, you understand where the smell came from.")
        print("The floor is littered with rotting corpses.")
        print("Suddenly you hear a growl and a huge zombie appears in front of you.")
        print("You see a passage to the east, a flaming torch on the ground,")
        print("a zombie holding a sword and a hole on the far side of the room.")
        print("The passage to the south leads to the second room.")
        print("What do you do?")
        print("Enter : east, torch, sword, hole or south")

        choice = input("> ")

        if "east" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""As you run towards the east passage, the zombie leaps
in front of you. You don't have the time to do anything,
because the zombie opens its jaws and rips of your head.""")
            game_over()
        elif "torch" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You take the flaming torch and wave it in front of the
zombie. It leaps back in fear, stumbles and falls in the
hole, disappearing from the room.""")
            zombie_alive = False
            room_3()
        elif "gun" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You take the gun. Suddenly, it starts emanating a faint
glow and you feel invincible. Without knowing how, you
jump forward and kill the zombie.""")
            zombie_alive = False
            gun = True
            room_3()
        elif "hole" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling.""")
            game_over()
        elif "south" in choice:
            room_2()
        else:
            room_3()

    else:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("The floor is littered with rotting corpses.")
        print("You see a passage to the east, a flaming torch on the ground,")
        print("a zombie holding a sword and a hole on the far side of the room.")
        print("The passage to the south leads to the second room.")
        print("What do you do?")
        print("Enter : east, torch, sword, hole or south")
        choice = input("> ")

        if "east" in choice:
            room_4()
        elif "torch" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You take the flaming torch and wave it in the air.
You feel stupid and put it down.""")
            room_3()
        elif "gun" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You take the sword.""")
            gun = True
            room_3()
        elif "hole" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
then you hit the floor. You die days immediately.""")
            game_over()
        elif "south" in choice:
            room_2()
        else:
            room_3()


def room_4():

    global Big_zombie_alive

    if Big_zombie_alive:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("In the room there's a big zombie.")
        print("Enter : gun, north, east, south or west")
        choice = input("> ")
        if "gun":
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""Suddenly you take your gun out of your bag. An unknown force urges you and you shoot
            the head of the big zombie. It dies with horrible screams.""")
            Big_zombie_alive = False
            room_4()
        else:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("There is a passage to the north, one to the east, one to the")
            print("south and one to the west. What do you do?")

            choice = input("> ")
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("The dragon leaps in front of you and roasts you alive.")
            game_over()
    else:
        print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
        print("There is a passage to the north, one to the east, one to the")
        print("south and one to the west. What do you do?")

        choice = input("> ")

        if "east" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""You follow the east passage until you end up in a little
room with a desk and a PC on it. A little fellow is typing
on the PC and suddenly he notices your presence. 'You should
not have found me, the coder of this game!' he says. 'Now
you have to die.' He types something on the PC, and you die.""")
            game_over()
        elif "south" in choice:
            room_1()
        elif "west" in choice:
            room_3()
        elif "north" in choice:
            print("ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ")
            print("""The passage leads to the surface.
             someone take your hand and take you in a helicopter. You are free! You have
won the game!""")
            win()
        else:
            room_4()


def start():
    room_1()


def win():

    global zombie_alive
    global Big_zombie_alive
    global gun

    zombie_alive = True
    Big_zombie_alive = True
    gun = False
    print("Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ ")
    print("You win")
    print("You can run away from the zombies")
    print ("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)


def game_over():

    global zombie_alive
    global Big_zombie_alive
    global gun

    zombie_alive = True
    Big_zombie_alive = True
    gun = False
    print("ƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔ")
    print("Game over")
    print("You are now a zombie")
    print ("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)


start()