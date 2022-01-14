
print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.\n")

name=input("What is your name?\n")                              # asks the users name and stores it in 'name' variable                         
if name=="Arthur" or name=="arthur" :                           #checks if name is equal to "Arthur" or arthur
    print("My Leige! You may pass!")                            #if so, king is allowed to pass and program ends
else:
    quest=input("What is your quest?\n")                        #if name is other than king's name, then quest of the user is asked and stored in 'quest' variable
    if "Grail" and "grail" not in quest:                        #checks whether user seeks 'grail or not
        print("Only those who seek the Grail may pass.")        #if not print function will execute and program ends
    else:
        color=input("What is your favorite color?\n")           # asks user to input his favorite color
        if color[0].upper()==name[0].upper():                   #checks whether first letter of color and name is equal
            print("You may pass")                               #if equal user able to pass the bridge and program ends
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")   #if not equal,he is not able to pass and program ends


