#!/usr/bin/python3

def main():
	fh = open('line.txt')
	for line in fh.readlines():
		print(line,end=" ")

	s = "I am a string"
	for i , c in enumerate(s):
		if c == "s": print( ' index {} is a string'.format(i))

if __name__ == "__main__": main()