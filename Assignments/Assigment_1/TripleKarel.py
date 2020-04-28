from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
Makes Karel move trough the walls and dorops beepers except 
the corbers. There are three cubs with different sizes. The dimension
of the world may vary.

Pre-condition: Karel always start with facing to the west, and
have infinite beepers

Post-condition: Karel is facing opposite direction 
to start position, at the corner of the last cube.
"""


def main():
    # This function will paint all three cubes
    for i in range(3):
        paint_wall()
        move_to_next()


"""
Karel paints the cube 3 sides of the cube
----------------------------------------------------
pro: at the beginning corner of the cub facing front
post: at the end of 3rd wall facing front
"""


def paint_wall():
    for i in range(2):
        paint_cell()
        turn_left()
        move()
    paint_cell()


"""
Karel paints the wall until left is blocked
-------------------------------------------
pro: at the begining of the wall
post: at the end of wall painted wall

"""


def paint_cell():
    while left_is_blocked():
        put_beeper()
        move()


"""
Karel moving to the next cube to be painted
-------------------------------------------
pre: Karel stands at the end of last painted cube
post: Karel stands of the recently painted cube 
"""


def move_to_next():
    if front_is_blocked():
        put_beeper()
        turn_right()
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__=="__main__":
    run_karel_program()
