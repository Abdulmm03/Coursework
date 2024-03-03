#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion
#Any code taken from other sources is referenced within my code solution

#IIT Student ID: 20221316
#Uow ID: w1956099

#Date : 1st Nov 2022


#Progression outcomes
progress_count = 0
progress_module_trailer_count = 0
Do_not_progress_count = 0
Exclude_count = 0

#lists
Progress=[]
Progress_module_trailer=[]
Module_Retriever=[]
Exclude=[]


quit_option = 'y'


def int_input(message,error_message):    #user defined function to prompt user for credits
            while True:
                try:
                    credit = int(input(message))
                    if credit>120 or credit<0 or credit % 20 != 0:
                        print('Out of range')   #Validation for range
                        continue
                except ValueError:
                    print(error_message) #Integer validation
                    continue
                break
            return credit


while quit_option != 'q':

        temp_student_details=[]             #list to store credits temporarily until verification
        
        cred_pass = int_input('Enter pass credits: ','Integer required')
        temp_student_details.append(cred_pass)
        cred_defer = int_input('Enter defer credits: ','Integer required')
        temp_student_details.append(cred_defer)
        cred_fail = int_input('Enter fail credits: ','Integer required')
        temp_student_details.append(cred_fail)
        

        if cred_pass + cred_defer + cred_fail != 120: 
              print('Total incorrect')
              continue


            
           #Verify Progression outcomes using common trends

        if cred_pass == 120:
             progress_count += 1
             Progress.append(temp_student_details) #Append credits stored in temporary list to progress list
             print('Progress\n')
            
                 

        elif cred_pass == 100:
             progress_module_trailer_count += 1
             Progress_module_trailer.append(temp_student_details) #Append credits stored in temporary list to Progress(Module trailer) list
             print('Progress(Module Trailer)\n')
            
                  
        elif 60>=cred_fail>=0:
             Do_not_progress_count += 1
             Module_Retriever.append(temp_student_details) #Append credits stored in temporary list to Module Retriever list
             print('Module retriever\n')

            
                 
        else:
             Exclude_count += 1
             Exclude.append(temp_student_details) #Append credits stored in temporary list to Exclude list
             print('Exclude\n')
            
                 
                        
                                 

        print()  #Predict multiple progression outcomes & loop
        print('Do you want to enter new data?')
        quit_option = input('Input "y" indicating yes or "q" to quit and view results: ')
        if quit_option not in("y","q"):
            print('Improper input')
        else:
            continue
            


        print()
        


#Histogram Design

design_1 = progress_count *'*'
design_2 = progress_module_trailer_count *'*'
design_3 = Do_not_progress_count *'*'
design_4 = Exclude_count *'*'

print('............................................................')



print('Histogram')

print('Progress', progress_count ,':', design_1 )
print('Trailer', progress_module_trailer_count ,':', design_2 )
print('Retriever', Do_not_progress_count,':', design_3 )
print('Excluded', Exclude_count ,':', design_4)

print()

outcomes = progress_count + progress_module_trailer_count + Do_not_progress_count + Exclude_count
print( outcomes,' Outcomes in Total ' )




print('............................................................')


#Lists for all 4 outcomes

for i in range(progress_count):
    print("Progress - ",Progress[i][0],", ",Progress[i][1],", ",Progress[i][2])

for i in range(progress_module_trailer_count):
    print("Progress(module trailer) - ",Progress_module_trailer[i][0],", ",Progress_module_trailer[i][1],", ",Progress_module_trailer[i][2])
    
for i in range(Do_not_progress_count):
    print("Module Retriever - ",Module_Retriever[i][0],", ",Module_Retriever[i][1],", ",Module_Retriever[i][2])
    
for i in range(Exclude_count):
    print("Exclude - ",Exclude[i][0],", ",Exclude[i][1],", ",Exclude[i][2])




#Text File(Extension) for all 4 outcomes

with open ('Progress_file.txt','w')as file:
    for i in Progress:
        file.write(f'{i}\n')
with open('Progress_module_trailer_file.txt','w')as file:
    for i in Progress_module_trailer:
        file.write(f'{i}\n')
with open ('Module_Retriever_file.txt','w')as file:
    for i in Module_Retriever:
        file.write(f'{i}\n')
with open('Exclude_file.txt','w')as file:
    for i in Exclude:
        file.write(f'{i}\n')

    

print()
        







    
















        


    
