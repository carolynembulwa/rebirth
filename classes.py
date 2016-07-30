#!/usr/bin/python3
class Duck:
	def __init__(self , **kwargs):
		self.variables = kwargs
	
	def quack(self):
		print('Quaaaack' )

	def walk(self):
		print('Am walking like a duck')

	def get_variable(self , k ):
		return self.variables.get(k ,None)

	def set_variable(self , k , v):
		self.variables[k] = v 

def main():
	donald = Duck(color = 'yellow' , feet = 4)
	tom = Duck(color = 'blue' , feet = 5)
	print(tom.get_variable('feet'))
	print(donald.get_variable('color'))
	tom.walk()
	tom.quack()
	donald.quack()
	donald.walk()


if __name__ == "__main__": main()