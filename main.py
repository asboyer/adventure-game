from boyer import *
from art import text2art
from os import path

speed = 0
# TO DO: read a file of highscores
#       if no highscores, make new file
highscore = 0
highlevel = 0
playing = True
played = 0


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
    death_file = f"deaths/death{str(choice)}_{str(level)}"

    if path.exists(f'text/{death_file}.txt'):
        delay_print(fr(death_file), speed)
        return False
    else:
        return True

def check_win(level, choice):
    win_file = f"wins/win{str(choice)}_{str(level)}"

    if path.exists(f'text/{win_file}.txt'):
        delay_print(fr(win_file), speed)
        return True
    else:
        return False

def check_bonus(level):
    bonus_file = f"bonus/bonus_{str(level)}"

    if path.exists(f'text/{bonus_file}.txt'):

        delay_print("bonus question!".upper())

        file = open(f"text/{bonus_file}.txt", "r")
        lines = file.readlines()
        answer = input(lines[0]).lower().strip()
        answers = lines[1].strip().split(" ")

        if answer in answers:
            return int(lines[2])
        else:
            return 0
    
    else:
        return 0  

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

def scorecard(score, level, played):
    print('\n_____________________________')
    print(f'Level reached: {str(level)}')
    print(f'Highest level: {str(highlevel)}')
    print(f'Games played: {str(played)}')
    print(f'Score: {str(score)}')
    print(f'Highscore: {str(highscore)}')
    print('_____________________________\n')

def credits():
    delay_print(fr('credits'), speed)

while playing:

    choice = ""
    score = 0
    alive = True
    win = False
    level = 1

    intro(played)

    while alive and not win:
        choice = choose(level, choice)
        score += check_bonus(level)
        alive = check_alive(level, choice)
        win = check_win(level, choice)
        if alive:
            score += int(1.5 * level)
            level += 1

    played += 1

    if win:
        delay_print("\nyou win!\n".upper(), speed)
        credits()

    else:
        delay_print("\ngame over\n".upper(), speed)

    if score > highscore:
        highscore = score
        print("new high score".upper())
        # enter initials

    if level > highlevel:
        highlevel = level
        print("new highest level".upper())

    scorecard(score, level, played)

    if not play_again():
        break
