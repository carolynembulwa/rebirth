#!/usr/bin/python3

def main():
	s  = "This is a string"
	for  c in s:
		if c == "s": continue
		print(c, end=' ')

	i = 0
	while(i < len(s)):
		print(s[i], end="")
		i += 1
	else:
		print( " I am done" )
if __name__ == "__main__": main()