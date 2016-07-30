#!/usr/bin/python3

class Duck:
	def quack(self):
		print('Quaaaack')

	def walk(self):
		print('Am walking like a duck')

	def bark(self):
		print("I cant bark you moron a am a duck")

	def clothes(self):
		print("I have feathers stupid  and I love it")

class Dog:
	def quack(self):
		print('How am i supposed to quack')
	
	def walk(self):
		print("Am walking like a dog")

	def bark(self):
		print("Woof woof!")

	def clothes(self):
		print("I have a some nice fur")

def in_the_pond(duck):
	duck.quack()

def in_the_forest(dog):
	dog.bark()


def main():
	donald = Duck()
	devlin = Dog()
	

	in_the_forest(devlin)
	in_the_pond(donald)

	# Looping through each functions available in each
	# for a in donald , devlin:

	# 	a.quack()
	# 	a.walk()
	# 	a.bark()
	# 	a.clothes()
	
if __name__ == "__main__": main()