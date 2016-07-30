#!/usr/bin/python3

def main():
	testfunc( 1 , 2 ,3 , 4 ,5 )
	testfunca(1 ,2, 3 ,4 ,one = 1 , two = 2 , seven = 7)
# multiple arguments rep by *args


def testfunc(that , *args):
	print(that , args)
	for i in args:
		print(i, end = "")

# Key word arguments to a fuction 

def testfunca(*args ,**kwargs):
	print(args ,kwargs['one'] , kwargs['two'] , kwargs['seven'])
if __name__ == "__main__": main()