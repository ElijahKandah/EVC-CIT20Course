import io

"""
	Student: Elijah Kandah
	Module: gladysUserLogin
	Description: This module allows the user to input an email and password before accessing the application 
"""

def login():
	emailAddress = input("Enter your email address:")
	lowerInput = emailAddress.lower()

	validEmail = False
	while (not validEmail):

		if (('@' in lowerInput) and (".com" in lowerInput)) :
			validEmail = True
		else :
			print("ERROR: Not a Valid Email Address")
			emailAddress = input("Enter your email address:")
			lowerInput = emailAddress.lower()

	password = input("Enter your password:")

	"""
		document your function definition here. what does it do?
	"""

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""

	"""
	emailAddress = "malcomx@mecca.com"
	"""
	return emailAddress
