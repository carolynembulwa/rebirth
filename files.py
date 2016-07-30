#!/usr/bin/python3

def main():
	f = open("line.txt")
	for line in f.readlines():
		print(line , end = " ")

if __name__ == "__main__": main()