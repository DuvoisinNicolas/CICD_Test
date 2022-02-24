def programIsWorking():
	return 1

def programIsntWorking():
	return -1

def myBadFunction(val):
	print("Doing many things...")
	print("Doing even more things...")
	val = 0
	print("But val got unexpectedly modified !")
	return val


def myFunction():
	result = -1
	shouldBeSetTo1 = 1
	shouldBeSetTo1 = myBadFunction(shouldBeSetTo1)
	if shouldBeSetTo1 == 1:
		result = programIsWorking()
	else:
		result = programIsntWorking()	
	
	return result

if __name__ == "__main__":
	myFunction()
