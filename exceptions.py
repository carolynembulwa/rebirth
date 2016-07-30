#!/usr/bin/python3

def main():
	
	try: 
		fh  = open('xline.txt')
	except:
		print('Could not find file. come back tomorrow')
	else:	
		for line in fh: print(line.strip())

if __name__ == "__main__": main()