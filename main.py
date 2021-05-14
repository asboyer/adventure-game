from boyer import *
from art import text2art
from os import path

speed = 0

def starter(played):
    if played == 0:
        # set the scene
        delay_print(fr('intro'), speed)
        print("\n")
        
    else:
        pass

def fr(name):
    file = open(f"text/{name}.txt", "r")
    return file.read()

def choose(level, choice):
    delay_print(fr(f'descriptions/description{str(choice)}_{str(level)}'), speed)

    return get_num(fr(f'choices/choice{str(choice)}_{str(level)}'), start=0, finish=1, integer=True)

def check_alive(level, choice):
    death_file = f"text/deaths/death{str(choice)}_{str(level)}"

    if path.exists(death_file):
        delay_print(fr(death_file), speed)
        return False
    else:
        return True

def check_win(level, choice):
    win_file = f"text/wins/win{str(choice)}_{str(level)}"

    if path.exists(win_file):
        delay_print(fr(win_file), speed)
        return True
    else:
        return False

def play_again():
    while True:
        choice = input("Play again? ")
        if choice.startswith('y'):
            return True
        elif choice.startswith('n'):
            return False
        else:
            print('Please enter a yes or no!')

def intro(played):
    clear()
    starter(played)
    delay_print("Welcome to...", speed)
    print(text2art("Boyer's\nadventure\ngame"))
    input("\nPress enter to begin\n")
    clear()

def scorecard(score, highscore, level, played, highlevel):
    print(f'Level reached: {str(level)}')
    print(f'Highest level: {str(highlevel)}')
    print(f'Games played: {str(played)}')
    print(f'Score: {str(score)}')
    print(f'Highscore: {str(highscore)}')

def credits():
    delay_print(fr('credits'), speed)

# TO DO: read a file of highscores
#       if no highscores, make new file
highscore = 0
highlevel = 0
playing = True
played = 0

while playing:

    choice = ""
    score = 0
    alive = True
    win = False
    level = 1

    intro(played)

    while alive and not win:
        choice = choose(level, choice)
        alive = check_alive(level, choice)
        if alive:
            score += 1.5 * level
            level += 1

    played += 1

    if win:
        delay_print("\nYOU WIN!", speed)
        credits()

    else:
        delay_print("\nGAME OVER", speed)

    if score > highscore:
        highscore = score
        print("NEW HIGH SCORE!")
        # enter initials

    if level > highlevel:
        highlevel = level
        print("NEW HIGHEST LEVEL")

    scorecard(score, highscore, level, played, highlevel)

    if not play_again():
        break






