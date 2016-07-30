#!/usr/bin/python3

def main():
	choices = dict(
		one =  "First" , 
		two = "Second"
		)
	v = 'one'
	d = "five"
	print(choices[v])
	print (choices.get(d, 'other'))

if __name__ == "__main__": main()