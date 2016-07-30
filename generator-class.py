#!/usr/bin/python3
class inclusive_range:
	# A constructor method
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: raise TypeError("Requires at least one argument")
		elif numargs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1
		elif numargs == 2 :
			(self.start, self.stop) = args
			self.step = 1
		elif numargs == 3:
			(self.start, self.stop , self.step) = args
		else: raise TypeError("Expected 3 arguments got {}".format(numargs))

	# An iterator method
	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i 
			i += self.step

def main():  
	# the inlusive range object has a inter method that works as an iterator
	for i in inclusive_range(2 ,25 ,6): 
		print(i , end=" ")


if __name__ == "__main__": main()