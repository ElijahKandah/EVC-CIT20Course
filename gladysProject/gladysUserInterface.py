import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Elijah Kandah
	Module: gladysUserInterface
	Description: This module acts as the starting point for the application. Here users start the program, allowing them to manipulate the menu
"""


def runTests():
	"""
		tests some module functions
	"""

	print("running a few tests")
	print("testing login")
	userLogin.login()
	print("testing readSat() function")
	pathToJSONDataFiles = "C:/Users/elija/OneDrive/Documents/GitHub/EVC-CIT20Course/gladysProject"
	data = satellite.readSat("altitude",pathToJSONDataFiles)
	print("readSat() Function compeleted")
	
	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules
	print("hello!")
	
def setCurrentPosition() :
	xInput = float(input("Enter a x:")) 
	print("Current x position is " + str(xInput))
	yInput = float(input("Enter a y:"))
	print("Current y position is " + str(yInput))
	print("Current position is (" + str(xInput) +"," + str(yInput) +")")
	return compute.gpsAverage(int(xInput),int(yInput))

def setDestinationPosition() :
	xInput = float(input("Enter a x:")) 
	print("Destination x position is " + str(xInput))
	yInput = float(input("Enter a y:"))
	print("Destination y position is " + str(yInput))
	print("Destination position is (" + str(xInput) +"," + str(yInput) +")")
	return compute.gpsAverage(int(xInput),int(yInput))

def getMapDistance(x,y) : 
	print(compute.distance(x,y))
	return compute.distance(x,y)

def start():
	"""
		logs the user in, and runs the app
	"""

	userName = userLogin.login()

	runApp(userName)


def runApp(userName):
	"""
		runs the app
	"""

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# menu
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("-- Welcome to the Gladys West Map App --")
		print("Type t to run tests")
		print("Type q to quit")
		print("Type c to set current position")
		print("Type d to set destination position")
		print("Type m to map")

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		"""
			here students need to change and add to this code to
			handle their menu options
		"""
		# quit
		if firstChar == 'q':
			userQuit = True

		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()
		elif firstChar == 'c':
			currentPosition = setCurrentPosition()
		elif firstChar == 'd':
			destinationPosition = setDestinationPosition()
		elif firstChar == 'm':
			getMapDistance(currentPosition,destinationPosition)

		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
