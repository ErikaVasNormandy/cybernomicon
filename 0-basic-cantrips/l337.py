import random

while(1): # Endless loop of user input
    l337String = "" # Empty string for user to return
    temporaryChar = "" # Placeholder

    inputstring = input("\nEnter a string:\n\n") # Prompt user for input

    for i in inputstring:
        if(i.isalpha()):
            capitalizeOrNot = random.randint(0,1) # Decide if we want to change it
            if(bool(capitalizeOrNot)): # We'll decide off the bat if we want to modify it
                holder = ord(i) # Gets the number for switching it to a different case
                if(i.isupper()):
                    # print("converted string is ", chr(holder+32))
                    # l337String+=chr(holder+32)
                    temporaryChar = chr(holder+32)
                elif(i.islower()):
                    # print("converted string is ", chr(holder-32))
                    # l337String+=chr(holder+32)
                    temporaryChar = chr(holder-32)
                l337String+=temporaryChar # once we're done modifying it, we'll add it ion

            else: ### in the scenario we decided not to modify it
                l337String+=i ## just add it
        else: 
            l337String+=i
    print("\n{}".format( l337String))
        

