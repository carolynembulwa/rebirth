#!/usr/bin/python3

def main():
	try:
		for line in readfile('laine.tx'): print(line.strip())
	except IOError as e:
		print("Cannot read file" , e)
	except ValueError as e:
		print('Invalid file extesion' ,e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh.readlines()
	else: raise ValueError('Filename must be a valid text file')
if __name__ == "__main__": main()