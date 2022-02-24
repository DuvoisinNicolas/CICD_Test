def programIsWorking():
	return 1

def programIsntWorking():
	return -1

def myFunction():
	result = -1
	shouldBeSetTo1 = 1
	if shouldBeSetTo1 == 1:
		result = programIsWorking()
	else:
		result = programIsntWorking()
	return result

if __name__ == "__main__":
	myFunction()
