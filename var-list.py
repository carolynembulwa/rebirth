#!/usr/bin/python3

def main():
	x = (1, 2, 4)
	y = [1, 2 ,3]
	y.append(45)
	y.insert(0 , 99)
	d =  {"one": 1 , "two" : 2}
	e = dict( one =  1 , two =  2 )
	e["sev"] = 7

	a , b = 2,2
	if a < b :
		print("True")
	else: 
		print("False")


	for k in sorted(e.keys()):
		print(k , e[k])
	for i in x:
		print(i)
	print (type(x) , x)
	print (type(y) , y)
	print(d)

if __name__ == "__main__": main()