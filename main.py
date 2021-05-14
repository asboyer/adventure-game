from boyer import *

def starter(played):
    if played == 0:
        # set the scene
        delay_print(fr('starter'))
    else:
        pass
        # you know the drill, run it back

def fr(name):
    file = open(f"descriptions/{name}.txt", "r")
    return file.read()

def choose(level, choice):
    delay_print(fr(f'choice{str(choice)}_{str(level)}'))
    print(f)

    return get_num(fr(f'description{str(choice)}_{str(level)}') + " ", start=0, finish=1, integer=True)

check_alive():

# read a file of highscores
# if no highscores, make new file
highscore = 0
playing = True
played = 0

while playing:
    # initializing variables
    choice = ""
    score = 0
    alive = True
    win = False
    level = 1

    clear()
    starter(played)

    while alive and not win:
        choice = choose(level)
        level += 1
        check_alive()

    if win:
        # winner
    else:
        # death
    # choice






