#%% First, let's create a menu with two options
# 1. enter your name
# 2. count the number of "a's" in your name and print it

loop = True
while loop == True:
    print("Please select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    opt = input('>>')
    if opt == "1":
        print('Please enter your name:')
        name = input('>>')
        print("Your name has been stored!")
    elif opt == "2":
        print("The number of a's in your name is:", name.count('a'))
    else:
        print("Incorrect option. Try again.")


#%% Then, we add an option "0" to exit the program

loop = True
while loop == True:    
    print("Please select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    print("Option 0: Exit")
    opt = input('>>')
    if opt == "1":
        print('Please enter your name:')
        name = input('>>')
        print("Your name has been stored!")
    elif opt == "2":
        print("The number of a's in your name is:", name.count('a'))
    elif opt == "0":
        print("bye!")
		loop = False
    
	
#%% Afterwards, we will allow the user only three attempts to select a valid option

counter = 0
loop = True
while loop == True and counter<3:    
    print("Please select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    print("Option 0: Exit")
    opt = input('>>')
    if opt == "1":
	# you could set counter=0 here to allow the user three more attempts
        print('Please enter your name:')
        name = input('>>')
        print("Your name has been stored!")
    elif opt == "2":
	# same here, counter=0 for three more chances
        print("The number of a's in your name is:", name.count('a'))
    elif opt == "0":
        print("bye!")
		loop = False
    else:
        counter = counter+1
        print("Incorrect option. Try again.")


#%% Now, option 1 must to be selected before option 2

counter = 0
memory = [] #create a memory list
loop = True
while loop == True and counter<3:    
    print("Please select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    print("Option 0: Exit")
    opt = input('>>')
    memory.append(opt)
    if opt == "1":
        print('Please enter your name:')
        name = input('>>')
        print("Your name has been stored!")
    elif opt == "2":
        if "1" in memory:
            print("The number of a's in your name is:", name.count('a'))
        else:
            print("Please select option 1 first")
    elif opt == "0":
        print("bye!")
		loop = False
    else:
        counter = counter+1
		# we will customise the error message
		if counter==3:
			print("Incorrect option. Program stops.")
		else:
			print("Incorrect option. Try again. You have tried "+str(counter)+' times!')

#%% We can add some more complexity to our programme, such as...
# the name must have more than 2 characters, otherwise try again / gets kicked out
# if the user enters an invalid name (numbers, blank or has a space), try again / gets kicked out

#%% More ideas
# Add a fourth option that displays all the names that have been stored before
# and their corresponding "a" letter count
# if this option is selected before 1 and 2, print "empty list"
# this option has to check that both 1 and 2 have been used before in that order

#%% Finally, give more robustness to our program
# Verify that the input in the main menu is a number
	# if an invalid number, print "invalid option"
	# if not a number, print "invalid input"