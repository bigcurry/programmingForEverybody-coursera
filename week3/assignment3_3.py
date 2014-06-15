''' Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.'''

grade = raw_input("Test Score: ")

try:
	grade = float(grade)

	if grade >= .9:
		letter = 'A'
	elif grade >= .8:
		letter = 'B'
	elif grade >= .7:
		letter = 'C'
	elif grade >= .6:
		letter = 'D'
	elif grade < .6:
		letter = 'F'
	else:
		letter = 'Invalid score input'

	print letter

except:
	print 'Test Score entered was not numeric!'