from karel.stanfordkarel import *


# File: hospital.py
# -----------------------------
# Here is a place to program your section problem
def main():
    for i in range(3):
        move_to_place()
        build_hospital()


def move_to_place():
    if no_beepers_present():
        move()
    while no_beepers_present():
        move()


def build_hospital():
    build_upside()
    build_downside()


def build_upside():
    turn_left()
    for i in range(2):
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    turn_right()


def build_downside():
    move()
    turn_right()
    for i in range(2):
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
    turn_left()
    if front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__=="__main__":
    run_karel_program()