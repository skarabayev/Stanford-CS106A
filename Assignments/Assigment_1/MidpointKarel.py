from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

"""
You should write your code to make Karel do its task in
this function. Make sure to delete the 'pass' line before
starting to write your own code. You should also delete this
comment and replace it with a better, more descriptive one.
"""

def main():

	fill_the_line()
	calculation_of_center()
	final_move()


def fill_the_line():
	"""
	Karel fill cells until the end of line. 1st and last cells are not filled
	-------------------------------------------------------------------------
	pre: Karel at the beginning of the line facing east
	post: Karel at the end of the line facing west
	"""
	move()
	while front_is_clear():
		if no_beepers_present():
			put_beeper()
			move()
		else:
			move()
	if front_is_blocked():
		turn_around()
		move()


def calculation_of_center():
	"""
	Karel picks beepers from the nearest cell and put beepers until the last filled cell
	------------------------------------------------------------------------------------
	pre: at the start of the filled cells without beepers in the bag
	post: at the end of filled cells with beepers in the bag
	"""
	if beepers_present():
		pick_beeper()
	move()
	while beepers_present():
		put_beeper()
		move()
		if no_beepers_present():
			turn_around()
			move()
			while beepers_present():
				pick_beeper()
			move()

def final_move():
	"""
	Karel puts the last beeper on its final position
	---------------------------------------------------
	pre: Karel facing west in the next cell from center
	post: Karel in the center of the line facing west
	"""
	turn_around()
	move()
	put_beeper()
	turn_around()

def turn_around():
	turn_left()
	turn_left()

if __name__ == "__main__":
	run_karel_program()
