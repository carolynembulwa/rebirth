#!/usr/bin/python3
# Decorators are special functions that
# return other functions

# used to create accesor methods for variables
class Panther:
	def __init__(self, **kwargs):
		self.properties = kwargs

	def growl(self):
		print("Grrrrrrr!")

	def walk(self):
		print("walks like a Panther")

	def get_properties(self):
		return self.properties

	def get_property(self, key):
		return self.properties.get(key , None)

	@property
	def color(self):
		return self.properties.get('color' , None)
	
	@color.setter
	def color(self , c):
		self.properties['color'] = c

	@color.deleter
	def color(self):
		del self.properties['color']

def main():
	maisie = Panther(color = 'blue')
	maisie.color  = 'blue'
	print(maisie.color)


if __name__ == "__main__": main()