print "Here you will find out whether you meet the requirements for a CS major at Wellesley."

def basic():
	answer = raw_input("Have you taken CS111?")
	if answer == 'yes' or 'Yes':
		print "You've taken the basic course!"
	else:
		print "Oops. You must take CS111 before moving onto intermediate courses."
		
def intermediate():
	answer = raw_input("Have you taken CS230?")
	if answer == 'yes' or 'Yes':
		new_answer = raw_input("Have you taken CS240?")
		if new_answer == 'yes' or 'Yes':
			print "You've taken the intermediates!"
		else:
			print "You need CS240 to continue."
	else:
		print "You need to start the intermediate courses." 
		
print basic()
print intermediate()
