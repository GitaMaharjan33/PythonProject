import csv                              #csv module imported to read the csv file
import sys                              #sys module imported to get command line argument

class league:
    '''Class created to read the files.'''
    data=[]                            #class variable created to store the list of match information
    countries=[]                       #class variable created to store the list of countries participating
    def __init__(self,filename1,filename2):                #default constructor
        with open(filename1,"r") as result_file:       #result file opened
            all_contents=csv.reader(result_file)       #file read with the help of reader function
            for line in all_contents:
                league.data.append(line)               #datas of the results file appended in the list 
        with open(filename2,"r") as team_file:            #file of cointries opened 
            for team in team_file:
                league.countries.append(team.strip())  #datas of the teams file appended in the list

class competition(league):                          #subclass of league class
    '''Class to calculate the result from the list of datas'''
    table_info=[]
    
    def __init__(self,filename1,filename2):
        super().__init__(filename1,filename2)                      #inherits the superclass
       
    def calulate(self):
        '''Function to calculate the played match,won match, draw match, scores and points of each countries.'''
        for country in league.countries:
            match_played=match_won=match_lost=match_draw=for_match=against_match=difference=points=0
            for data in league.data:
                if country  in data:
                    match_played+=1                 #match played will be incremented by 1 when country in in the data
                
                    goal_index1=data.index(country)+1   #cheked inde of the score of the country
                    goal_index2=4-goal_index1

                    if (int(data[goal_index1])>int(data[goal_index2])): # scores compared if country score is greater
                        match_won+=1
                        for_match+=int(data[goal_index1])
                        against_match+=int(data[goal_index2])
                        points+=3

                    elif(int(data[goal_index1])<int(data[goal_index2])):  #scores compared if country score is lesser
                        match_lost+=1
                        for_match+=int(data[goal_index1])
                        against_match+=int(data[goal_index2])
                    else:
                        match_draw+=1                                     # if scores of both country is equal
                        for_match+=int(data[goal_index1])
                        against_match+=int(data[goal_index2])
                        points+=1
                    difference=for_match-against_match
            #data of country stored on the list  
            competition.table_info.append([country,match_played,match_won,match_draw,match_lost,for_match, against_match,difference,points])

    def sort(self):
        '''Sorts data regarding points, difference and total scores'''
        for i in range(0,len(competition.table_info)-1):
            for j in range(i+1,len(competition.table_info)):
                if (competition.table_info[i][8]<competition.table_info[j][8]):     # manages the table on descending order on the basis of points
                    temp=competition.table_info[i]
                    competition.table_info[i]=competition.table_info[j]
                    competition.table_info[j]=temp
                elif(competition.table_info[i][8]==competition.table_info[j][8]):   #checks if points are same of countries
                    if (competition.table_info[i][7]<competition.table_info[j][7]): # manage the table on descending order on the basis of difference points
                        temp=competition.table_info[i]
                        competition.table_info[i]=competition.table_info[j]
                        competition.table_info[j]=temp
                    elif(competition.table_info[i][7]==competition.table_info[j][7]):   #checks if difference points are same of countries
                        if (competition.table_info[i][5]<competition.table_info[j][5]): ## manages the table on descending order on the basis of total golas by the team
                            temp=competition.table_info[i]
                            competition.table_info[i]=competition.table_info[j]
                            competition.table_info[j]=temp
               
    def table(self):
        '''Table that shows the results of the match'''
        print("%-15s %-6s %-6s %-6s %-6s %-6s %-6s %-6s %-6s" %("country","p","W","D","L","F","A","DIFF","PTS"))
        for value in competition.table_info:
            print("%-15s %-6s %-6s %-6s %-6s %-6s %-6s %-6s %-6s" %(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8]))

if __name__=="__main__":                  #runs only if file is not imported
    argument=sys.argv[1:]
    if len(argument)==0:
        scores=competition("results.csv","teams.csv")
    else:
        if argument[0]=="Six Nation 2021":              #command line argument for six nation 
            print(argument[0])
            print("="*len(argument[0]))
            scores=competition("results.csv","teams.csv")
        elif argument[0]=="Euro 2020 Group D":           #command line argument for four nation 
            print(argument[0])
            print("="*len(argument[0]))
            scores=competition("results2.csv","teams2.csv")
    
    scores.calulate()
    scores.sort()
    scores.table()

       