#%% First, lets create a menu with two options
# 1. enter your name
# 2. count the number of "a's" in your name and show it


opt = True
while opt == True:
    print("Please select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    opt = input('>>')
    if opt == "1":
        print('Please enter your name:')
        name = input('>>')
        print("Your name has been stored!")
        opt = True
    elif opt == "2":
        print("The number of a's in your name is:", name.count('a'))
        opt = True
    else:
        print("Incorrect option. Try again.")
        opt = True
        

#%% Then, we add the option "0" to exit the program
# Also, option 1 has to be selected before option 2

counter = 0
memory = [] #create a memory list
opt = True
while opt == True and counter<3:    
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
        opt = True
    elif opt == "2":
        if "1" in memory:
            print("The number of a's in your name is:", name.count('a'))
        else:
            print("Please select option 1 first")
        opt = True
    elif opt == "0":
        print("bye!")
    else:
        counter = counter+1
        print("Incorrect option. Try again.")
        opt = True




#%% Then, we add some complexity
# the name must have more than 2 characters
# if the user enters an invalid name (if it has numbers), gets kicked out

#%% Finally, we give more robustness to our program
# give three opportunities for the name before "kick out"
# Verify that the input in the main menu is a number
# if a number, print "invalid option"
# if not a number, print "invalid input"

#%% More ideas
# Add a third option that displays all the names that have been stored before
# and their corresponding "a" letter count
# if this option is selected before 1 and 2, print "empty list"
# this option has to check that both 1 and 2 have been used before in that order