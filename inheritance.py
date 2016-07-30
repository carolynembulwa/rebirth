#!/usr/bin/python3
class Animal:
	def talk(self): print("I have something to say")
	def walk(self): print("Hey I can walk")
	def clothes(self): print("Finally I have some clothes")

class Duck(Animal):
	def quack(self):
		print('Quaaaack')

	def walk(self):
		super().walk()
		print('Am walking like a duck')

class Dog(Animal):
	pass


def main():
	donald = Duck()
	donald.quack()
	donald.walk()
	donald.talk()

	devlin = Dog()
	devlin.clothes()
if __name__ == "__main__": main()