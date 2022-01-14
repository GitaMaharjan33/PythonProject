from statistics import mean

print("Swallow Speed Analysis: Version 1.0")
conversion = 1.60934                            #1 mph = 1.60934 kph

def swallow_speed():
    '''Function to find the maximum speed, minimum speed and mean speeds of the swallows in the British and in Europe. '''
    total_readings = []                             # created empty list that will contain the total readings done
    while True:                                 
        reading = input("Enter the Next Reading: ") #asks user to input the reading
        
        if reading:                                 #checks if reading is entered
            if reading[0] == "E" or reading[0] == "U":  #checks if entered reading starts with "E" or "U"
                total_readings.append(reading)      #reading is appended to 'total_reading' list
                print("Reading saved.")
            else:                                   
                print("It only accepts European and British reading.")  #printed if reading doesnot start with "E" or "U"
        
        else:                                       # this part will execute only if there is no reading
            if len(total_readings) == 0:              #checks if length of the list is zero
                print("No readings entered. Nothing to do.")
                exit()                              # if length of the list is zero program will terminate
            break
            
    print("\nResults Summary\n")
    No_Of_Reading = len(total_readings)             #stores the length of the list in variable "No_Of_Reading"
    
    #checks if number of reading is greater than one or not and  prints accordingly
    print((f"{No_Of_Reading} Reading Analysed.\n") if (No_Of_Reading == 1) else (f"{No_Of_Reading} Readings Analysed.\n"))

    speeds_mph = []                                   #created empty list to store speeds on mph unit
    for speed in total_readings:                      # iterated over list of total readings   
        if speed.startswith("E"):                     # checks if the speed is of European swallows
            speeds_mph.append(float(speed[1:])/conversion)    #string except first letter is typecasted and converted speed is appended to list "speeds_mph"
        elif speed.startswith("U"):                 #checks if speed is of British swallows
            speeds_mph.append(float(speed[1:]))      #string except first letter is typecasted and speed is appended to the list "speeds_mph"

    #executed if list containing speed is not empty
    if (speeds_mph != []):
        max_value = max(speeds_mph)                 #calculates maximum speed in mph with max function           
        print(f"Max speed:{max_value:.1f} MPH, {(max_value*conversion):.1f} KPH")
        min_value = min(speeds_mph)                 #calculates minimum speed in mph with min function  
        print(f"Min speed:{min_value:.1f} MPH, {(min_value*conversion):.1f} KPH")
        ave_value = mean(speeds_mph)                #calculates average speed in mph with mean function  
        print(f"Avg speed:{ave_value:.1f} MPH, {(ave_value*conversion):.1f} KPH")

        
if __name__ == "__main__":              
    swallow_speed()                                 #function called only if file was run directly