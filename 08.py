import random 

num = random.randint(0, 9)
players = ()
no_of_players = int(input("How many numbers of players are there? "))
user_player = input("Enter the 1st players name:")
list = user_player.split(" ")

if num == 0:
    print("dot ball")
elif num == 1:
    print("out")
elif num == 2:
    print("six!")
elif num == 3:
    print("one run!")
elif num == 4:
    print("no ball!")
elif num == 5:
    print("run out!")
elif num == 6:
    print("three run!")
elif num == 7:
    print("two run!")
elif num == 8:
    print("catch out!")
elif num == 9:
    print("six!")