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

def check_alive(level, choice):
    if level == 1 and choice == 1:
        delay_print(fr(f'death{str(choice)}_{str(level)}'))
        return False
    else:
        return True


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
        alive = check_alive()
        if alive:
            score += 1.5 * level
            level += 1

    if win:
        delay_print("YOU WIN!")
        # winner
    else:
        delay_print("GAME OVER")
        # death
    if score > highscore:
        highscore = score
        print("NEW HIGH SCORE!")
        # enter initials

    # play again?
    break






