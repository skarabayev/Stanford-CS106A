from karel.stanfordkarel import *


def main():
    for i in range(3):
        move()
    turn_left()
    move()
    move()
    move()
    put_beeper()
    move()
    put_beeper()
    for i in range(2):
        turn_right()
        move()
        put_beeper()
    for i in range(3):
        move()
    turn_left()
    for i in range(5):
        while front_is_clear():
            move()
            if no_beepers_present():
                put_beeper()
        turn_left()
    for i in range(4):
        while front_is_clear():
            move()
            if beepers_present():
                pick_beeper()
        turn_left()
    for i in range(3):
        move()
    turn_left()
    for i in range(3):
        move()
    for i in range(4):
        pick_beeper()
        move()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def run_karel_program():
    pass


if __name__=="__main__":
    run_karel_program()
