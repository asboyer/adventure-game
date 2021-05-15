from boyer import *
from art import text2art
from os import path

speed = 4
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
    print('\n')
    delay_print(fr(f'descriptions/description{str(level)}_{str(choice)}'), speed)
    print('\n')
    return get_num(fr(f'choices/choice{str(level)}_{str(choice)}'), start=0, finish=1, integer=True)

def check_alive(level, choice):
    death_file = f"deaths/death{str(level)}_{str(choice)}"

    if path.exists(f'text/{death_file}.txt'):
        delay_print(fr(death_file), speed)
        return False
    else:
        return True

def check_win(level, choice):
    win_file = f"wins/win{str(level)}_{str(choice)}"

    if path.exists(f'text/{win_file}.txt'):
        delay_print(fr(win_file), speed)
        return True
    else:
        return False

def check_bonus(level):
    bonus_file = f"bonus/bonus_{str(level)}"

    if path.exists(f'text/{bonus_file}.txt'):

        clear()
        delay_print("bonus question!".upper(), speed)
        print('\n')

        file = open(f"text/{bonus_file}.txt", "r")
        lines = file.readlines()
        answer = input(lines[0].strip() + " ").lower().strip()
        answers = lines[1].strip().lower().split(" ")

        if answer in answers or answer == lines[1].strip().lower():
            delay_print(f'Correct! You receive {lines[2]} points!', speed)
            clear()
            return int(lines[2])
        else:
            delay_print('Incorrect! You missed out on some bonus points!', speed)
            clear()
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
    choices = ""
    score = 0
    alive = True
    win = False
    level = 1

    intro(played)

    while alive and not win:
        score += check_bonus(level)
        choice = choose(level, choices)
        choices += str(choice)
        alive = check_alive(level, choices)
        win = check_win(level, choices)
        if alive and not win:
            score += int(1.5 * level)
            level += 1
        if win:
            score += int(1.5 * level)

    played += 1

    if win:
        delay_print("\nyou win!\n".upper(), speed)
        score += 1000 * level
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
