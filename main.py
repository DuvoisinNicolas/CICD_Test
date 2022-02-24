
def programIsWorking():
	print("OK")

def programIsntWorking():
	print("KO")

if __name == "__main__":
	shouldBeTo1 = 1
	if shouldBeTo1 == 1:
		programIsWorking()
	else:
		programIsntWorking()
