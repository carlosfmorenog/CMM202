counter = 0
flag = 0
memory = []
list_names = []
loop = True
while loop == True and counter<3:    
    print("\nPlease select your option")
    print('Option 1: Enter your name')
    print("Option 2: Count a's in your name")
    print("Option 3: Show history")
    print("Option 0: Exit")
    opt = input('>>')
    try:
        int(opt)
        memory.append(opt)
        if opt == "1":        
            name = True
            while name == True:
                print('Please enter your name:')
                name = input('>>')
                if len(name)>2 and "0" not in name and "1" not in name and "2" not in name and "3" not in name and "4" not in name and "5" not in name and "6" not in name and "7" not in name and "8" not in name and "9" not in name: # the name must have more than 2 characters and not contain numbers
                    print("Your name has been stored!")
                    flag = 1
                else:
                    print("Name must be larger than 2 characters and not contain numbers, please try again.")
                    name = True
        elif opt == "2":
            if "1" in memory and flag == 1:
                print("The number of a's in your name is:", name.count('a'))
                list_names.append((name,name.count('a')))
                flag = 0
            else:
                print("Please select option 1 first")
                memory = []
        elif opt == "3":
            if "1" in memory and "2" in memory:
                if memory.index("1")<memory.index("2"):
                    print(list_names)
                else:
                    print('Select option 1 first and then option 2!')
            else:
                print("Please select option 1 and 2 first")
        elif opt == "0":
            print("bye!")
			loop = False
        else:
            print("Invalid option. Try again.")
            counter = counter+1            
            print("Number of incorrect tries: ", counter)
    except ValueError:
        print("Invalid input. Try again")
        counter = counter+1            
        print("Number of incorrect tries: ", counter)
