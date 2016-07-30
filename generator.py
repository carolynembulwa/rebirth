#!/usr/bin/python3

def main():
	print("This is a syntax.py file")
	for x in inclusive_range():
		print(x , end= ' ')


def inclusive_range(*args):
	numargs = len(args)
	if numargs < 1 : raise TypeError("Requires at least one argument")
	elif numargs == 1:
		stop  = args[0]
		start = 0
		step = 1
	elif numargs == 2:
		(start , stop) = args
		step = 1
	elif numargs == 3:
		(start, stop , step) = args
	else: raise TypeError('inclusive range expected 3 got {}'.format(numargs))

	x = start
	while x <= stop:
		yield x 
		x += step


if __name__ == "__main__": main()