#!/usr/bin/python3

# use pypi for all python external libraries

import sys

def main():
	print("Python version {}.{}.{}".format(*sys.version_info))
	print(sys.platform)

	# import os

	# print(os.name)
	# print(os.getenv("PATH"))
	# print(os.getcwd())

	# import urllib.request
	# page = urllib.request.urlopen('http://iamcaleberic.github.io')
	# for line in page: print(str(line , encoding  = 'utf_8' ), end=" ")

	import random
	print(random.randint(1,1000))

	x = list(range(24))
	print(x)
	random.shuffle(x)
	print(x)

	import datetime
	now =  datetime.datetime.now()
	print(now)
	print(now.year , now.day)


if __name__ == "__main__": main()