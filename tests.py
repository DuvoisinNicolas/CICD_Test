#test_tests.py
from main import myFunction

def test_printOk():
	assert(myFunction() == 1)
