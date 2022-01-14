from random import choice

print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")

operator_names=["Janice","Fiona","Arthur","John","Jasmine"]          #operator names stored in list
#random phrases stored on tuple
any_random_phrases=("hmmmmmm","Oh, yes, I see","Tell me more","No please","You should try working on this system","Thats interesting")
end_message=["Bye","Goodbye","thanks","help","exit","quit"]     #chat ending words stored in list

#questioned that might be asked is on keys as a tuple and responses on values as a list and applying choice function to generate one response only
questions_response={("library","books"):choice(["Library will be closed for 1 month.","Library is destroyed.","No library for now.","No boooks."]),
        ("deadline","submission"):choice(["Late submission is okay.","Your deadline has been extended by two working days.","Submit later."]),
        ("Wifi","internet"):choice(["WiFi is excellent across the campus.","Internet is not poor.","turn off and on router."]),
        ("cafe","tea"):choice(["Cafe will open at 7 am.","More dishes on cafe.","Special tea available."]),
        ("Sports","games"):choice(["Play sports on monday.","No sports on tuesday.","Bring sports materials."]),
        ("car","bike"):choice(["There is no parking in college.","You cant bring vehicles  at school.","parking construction going on."])
        }
#list of boolean values to provide network errors
network_error=[True,True,False,True,True,True,True,True,True,True]

email_address=input("Please enter your Poppleton email address: ")      #asks user to input their email address of "The University of Poppleton"

def system_chat():
    '''Function to answer the question of the students by checking the validity of their email address.'''
    if email_address.count("@")==1:                                     #checks if email address has just one '@' or not
        index=email_address.find("@")                                   #to find the index of '@' on the email address
        if email_address[index+1:]=="pop.ac.uk" and index>2:            #to check whether there is domain after'@' or not and checks if there is more than 2 letters before '@'
            print(f"Hi,{email_address[:index].capitalize()}! Thank you, and Welcome to popChat!")   #sliced out the name of the student which is before '@'
            print(f"My name is {choice(operator_names)}, and it will be my pleasure to help you.")       #chose operators name using choice function

            while True:
                question=input("---> ")                                 #asks student to enter the question
                q_list=question.lower().split()                         #question changed to lowercase and splited 
                
                for key in questions_response:                          #iterating over dictionary
                    if(key[0].lower() in q_list or key[1].lower() in q_list):   #checks if values in tuples exists on the question
                        print(questions_response[key])                          #if exists, value of that key is printed
                        break
                else:
                    for message in end_message:                         #iterating over list of ending messages
                        if(message.lower() in q_list):                  #checks if message of list is in question
                            print(f"Thanks, {email_address[:index].capitalize()}, for using PopChat. See you again soon!")  
                            exit()                                      #program is terminated
                    else:
                        print(choice(any_random_phrases))

                if choice(network_error)==False:                        # if random value is false..network error will bw displayed
                    print("Network Error")
                    exit()                                              # then program is terminated
                
        else:
            #displayed if email address donot contains required domain or charcters before '@' is 2 or less than 2
            print("your name should be greater than two words and your domain maybe invalid.")  

    else:
        #displayed when there is no one '@'
        print("Your email_address is invalid.")

if __name__=="__main__":
    system_chat()                               #function called only if file was run directly