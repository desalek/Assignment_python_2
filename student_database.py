
"""
@uthored by:
    GROUP _____
    
       MEMBERS                               ID_№
    
    1. Asmamaw Abeba ----------------------> 1401399
    2. Bethlehem Sintayehu ----------------> 140
    3. Desale Kisi ------------------------> 140
    4. Milkay Arega -----------------------> 140
    
"""    



import sys

# function to display the menu option 
def menu():
    print("\n\t STUDENT MANAGEMENT SYSTEM")
    print("*"*40)
    print("1. Registration ")   
    print("2. search student based on id number") 
    print("3. update student name based on id")
    print("4. update student CGPA based on id")
    print("5. count total students in the system")
    print("6. count male and female numbers in the system")
    print("7. delete student from the system based on id")
    print("8. Top scorer students from each department")
    print("9. Top female scorer students from each department")
    print("10. search number of students based on gpa or gpa threshold")
    print("11. frequency of student names in the file")
    print("12. Number of students in each department")
    print("13. Display all students information")    
    print("14. delete all data")
    print("0. Exit\n")
    
    while True:  
        try:  
            choice = int(input("\n Enter your choice: "))
            # Mapping user choices to corresponding functions by using dictionary 
            choice_functions = {
                1: registration,
                2: search_student,
                3: updateName,
                4: updateCGPA,
                5: totalStudents,
                6: countMaleFemale,
                7: del_student,
                8: topScorerFrom_dept,
                9: top_female_scorer_depatment,
               10: gpa_threshold,
               11: st_frequent_name,
               12: numOfstudents_per_department,
               13: show_all,
               14: delete_all_data,
                0: Exit
               # Adding more choices can be done here
            }
            
            selected_function = choice_functions.get(choice)
            if selected_function:
                selected_function()
            else:
                print("👉Invalid choice! Choice is possible between 0 and 14 included them.")
        except ValueError:
            print("\n👉Invalid input, String type 'choice'  is not supported, try with integer...")
    menu()



  
  
# 1.function to register students 
def registration():
    with open("student_db.txt", "a+") as file:
        lines = file.readlines()
    # accepting unique student id number 
    while True:
        s_id = input("\nEnter student id: ")
        found = False
        for line in lines:
            try:# handle the file format error(how the file is formatted?)
                st_id, st_name, gender, dept, gpa = line.split(';')
                if s_id == st_id:
                    print("👉 ERROR: Student already exists. Try again.")
                    found = True
                    break
            except ValueError:
                continue
        if not found:
            break
    # accept name,gender and department     
    st_name = input("Enter student name: ")
    gender = input("Enter the student Gender: ")
    dept = input("Enter student department: ")
    # accepting student gpa which value is between 0 and 4 included and non String 
    while True:
        try: # handle ValueError 
            gpa = float(input("Enter student CGPA: "))
            if gpa > 4 or gpa < 0:
                print("\n👉sorry, student gpa shouldn't above 4(four) and below 0(zero)")
            else:
                break    
        except ValueError:
            print("\n👉Invalid input, String type GPA  is not supported, try with float..")
    # append the student information to the file system 
    with open("student_db.txt", "a") as file:
        file.writelines(f"{s_id};{st_name};{gender};{dept};{str(gpa)}\n")
    print("Registration is Ended successfully.")      
    menu()




    
#2. function to search student based on id number 
def search_student():
    with open("student_db.txt", 'r') as file:
        lines = file.readlines()
        id_search = input("Enter student ID to search: ")
        found = False
        for line in lines:
            try:# handle the file format error(how the file is formatted?)
                st_id, st_name, gender, dept, gpa = line.strip().split(';')
                if st_id == id_search:
                     print("-"*40)
                     print("\n\t Data found ")
                     print("-"*40)
                     print(f"Name: {st_name}\n Gender: {gender}\n Department: {dept}\n CGPA: {gpa}")
                     print("-"*40)
                     found = True
            except ValueError:
                continue 
        if not found:
            print("👉Student does not exist")
    menu()


    
#3. function to update student name based on id number 
def updateName():
    updated = False 
    lines = []
    id = input("Enter student id you want update : ")
    with open("student_db.txt", 'r') as file:
        for line in file:
            try: # handle the file format error(how the file is formatted?)
                st_id,st_name,gender,dept,gpa = line.split(';')
                if st_id == id:
                    new_name = input("Enter student new name: ")
                    line = f"{st_id};{new_name};{gender};{dept};{gpa}\n"
                    updated = True 
                lines.append(line)   
            except ValueError:
                continue  
        if not updated:
            print(f"👉Student with ID {id} not found.")
        else:
            print("update successfully!!")
            with open("student_db.txt", 'w') as file:
                file.writelines(lines)
    menu()
    
    
# 4.function to update student gpa based on id number 
def updateCGPA():
    updated = False
    lines = [] 
    id = input("Enter student id you want to update: ")
    with open("student_db.txt", 'r') as file:
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                st_id, st_name, gender, dept, gpa = line.split(';')
                if st_id == id:
                    while True:
                        try:
                            new_gpa = float(input("Enter student new GPA: "))
                            if new_gpa > 4 or new_gpa < 0:
                                print("\n👉sorry, student gpa shouldn't above 4(four) and below 0(zero)")
                            else:
                                break    
                        except ValueError:
                            print("\n👉Invalid input, String type GPA  is not supported, try with float..")
                    line = f"{st_id};{st_name};{gender};{dept};{str(new_gpa)}\n"
                    lines.append(line)
                    updated = True
            except ValueError:
                continue      
        if not updated:
            print(f"👉Student with ID {id} not found.")
        else:
            print("Update successful!")
            with open("student_db.txt", 'w') as file:
                file.writelines(lines)
    menu()
    
    
    


# 5. function to count all students 
def totalStudents():
    count = 0
    with open("student_db.txt","r") as file:
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid,name,gender,dept,gpa = line.split(";")
                count += 1
            except ValueError: 
                continue 
    print(f"👉 TOTAL NUMBER OF STUDENTS = {count}")
    menu()





# 6.function to count all males and females students 
def countMaleFemale():
    with open("student_db.txt","r") as file:
        countMale = 0
        countFemale = 0
        for line in file:
            try:# handle the file format error(how the file is formatted?)
               st_id,name,gender,dep,gpa = line.split(";")
               gender = gender.lower()
               if gender == "male" or gender == "m":
                   countMale += 1
               elif gender == "female" or gender == "f":
                   countFemale += 1
               else:  
                   print("Invalid gender. ")  
                   continue
            except ValueError:
                continue      
        print(f"👉 Total number of male students: {countMale}")
        print(f"👉 Total number of female students: {countFemale}")
    menu()
  
  


# 7.function to delete student information based on id number 
def del_student():
    st_id = input("Enter student ID: ")
    deleted = False
    lines =[]
    with open("student_db.txt", 'r') as file:
         for line in file:
             try:# handle the file format error(how the file is formatted?)
                stid,name,gender,dept,gpa = line.split(";")
                if st_id != stid:
                    line = f"{stid};{name};{gender};{dept};{gpa}\n"
                    lines.append(line)
                    continue
                else:     
                    deleted = True 
             except ValueError:
                 print("Invalid file line format.")
                 continue     
         if not deleted:
             print(f"Student with ID '{st_id}' not found.")
         else:
             with open("student_db.txt", 'w') as file:
                  file.writelines(lines)
             print(f"Student information with ID '{st_id}' is deleted successfully. ")
    print("\n THE REMAINING STUDENTS INFO...\n look 👇👇👇 here:")         
    show_all()    
    menu()
  
  
  

# 8. function to get scorer students from user input department(which is already existed department) 
def topScorerFrom_dept():
    with open("student_db.txt", "r") as file:
        dept_set = set()
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid, name, gender, dept, gpa = line.split(";")
                dept_set.add(dept)
            except ValueError:
                continue
    # users input department and check if it is occurred in the file 
    st_dept = input(f"Enter the department from {dept_set},which you want: ")
    if dept_set == set():
        print("👉 sorry! the file is empty.")   
        return
    if not st_dept in dept_set:
        print(f"\n👉 Sorry! The department '{st_dept}' doesn't exist in {dept_set} or in file.Is it empty set ? if not choose from displayed one.\n")
        topScorerFrom_dept() 
    # variables which are used to identify the student, which are talented 
    found = False
    max_gpa = 0
    scorer_name = [] #list to stothe scorer student name   
    #find the scorer students for user input department(st_dept) from the system iteratively 
    with open("student_db.txt", "r") as file:
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid, name, gender, dept, gpa = line.split(";")
                if st_dept == dept and float(gpa) > max_gpa:
                    max_gpa = float(gpa)
                    scorer_name = [name.upper()]
                elif st_dept == dept and float(gpa) == max_gpa:
                    scorer_name.append(name.upper())
                found = True
            except ValueError:
                continue
        if not found:
            print(f"\nThe department {st_dept} that you entered doesn't exist or has no registered students.")
        else:
            print(f"\n👉 TOP SCORING STUDENT(s) IN {st_dept} DEPARTMENT: ")
            print("="*43)
            print(f"Scorer Names: {', '.join(scorer_name)}")
            print(f"With GPA: {max_gpa}")
    menu()
    
    
    
    
    
    
    
# 9.function to get female scorer students from user input department(which is already existed department) 
def top_female_scorer_depatment():
    dept_set = set() # A set of department in a file 
    with open("student_db.txt", "r") as file:
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid,name,gender,dept,gpa = line.split(";")
                dept_set.add(dept)
            except ValueError:
                continue  
    # users input department and check if it is occurred in the file          
    st_dept = input(f"Enter the department from {dept_set},which you want: ")
    if dept_set == set():
        print("👉 sorry! the file is empty.")   
        return
    if not st_dept in dept_set:
        print(f"\n👉 Sorry! The department '{st_dept}' doesn't exist in {dept_set} or in file. Is it empty set ? if not choose from displayed one.\n")
        top_female_scorer_depatment() 
    # variables which are used to identify the student, which are talented 
    found = False 
    max_gpa = 0
    scorer_name = []
    # find the scorer students for user input department(st_dept) from the system iteratively  
    with open("student_db.txt", "r") as file:  
        for line in file:
            try: # handle the file format error(how the file is formatted?)
                stid, name, gender, dept, gpa = line.split(";")
                if st_dept == dept and float(gpa) > max_gpa:
                    if gender == "female" or gender == "f":
                        max_gpa = float(gpa)
                        scorer_name = [name.upper()]
                        found = True 
                elif st_dept == dept and float(gpa) == max_gpa:
                    if  gender == "f" or gender == "female":
                        scorer_name.append(name.upper())
                        found = True 
                else:
                    continue   
                    found = True 
            except ValueError:
                continue  
        if not found:
            print(f"\n👉 There is no female students in '{st_dept}' department.")
        else:  
            print(f"\n👉 Top female scoring student(s) from '{st_dept}' department:\n Names: {','.join(scorer_name)} with GPA: {max_gpa}\n")    
    menu()





# 10 function to print student name with gpa they have greater gpa than  user gpa
def gpa_threshold():
    found = False 
    with open("student_db.txt", "r") as file:
        while True:
            try: # handle the file format error(how the file is formatted?)
                st_gpa = float(input("Enter the gpa: "))
                if st_gpa > 4 or st_gpa < 0:
                    print("\n👉sorry, student gpa shouldn't above 4(four) and below 0(zero)")
                else:
                    break    
            except ValueError:
                print("\n👉Invalid input, String type GPA  is not supported, try with float..")
        print(f"\nTop scoring students that greater than {st_gpa} GPA are: ")
        print("*"*43)
        for line in file:
            try: # handle the file format error(how the file is formatted?)
                stid, name, gender, dep, gpa = line.split(";")
                if float(gpa) > st_gpa:
                    print(f"👍 yes, {name}'s  gpa > {st_gpa}, which is {gpa}")   
                else:
                    print(f"👎 No, {name}'s  gpa  <= {st_gpa}, which is {gpa}")    
                found = True 
            except ValueError:
                continue   
        if not found:
            print("👉 sorry! the file is empty.")      
    menu()






# 11. function to count the frequency of unique names in the file 
def st_frequent_name():
    student_name_frequency = {}
    found = False 
    with open("student_db.txt", "r") as file:
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid, name, gender, dep, gpa = line.split(";")
                name = name.upper()
                if name in student_name_frequency:
                    student_name_frequency[name] += 1
                else:
                    student_name_frequency[name] = 1
                found = True 
            except ValueError:
                continue  
        if not found:
            print("👉 Sorry! there is no students in the file. ")   
        else:       
            print("\nName \t\t Frequency")
            print("*"*35)        
            for name,count in student_name_frequency.items(): 
                print( f"{name} \t\t {count} times frequent. " )
    menu()     



#12. function to count number of students in each department 
def numOfstudents_per_department():
    student_frequency = {}
    with open("student_db.txt", "r") as file:
        found = False 
        for line in file:
            try:# handle the file format error(how the file is formatted?)
                stid, name, gender, dept, gpa = line.split(";")
                if dept in student_frequency:
                    student_frequency[dept] += 1
                else:
                    student_frequency[dept] = 1
                found = True   
            except ValueError:
                continue   
        if not found:
            print("👉 The file is empty.")    
        else:
            print("\n Number of students in each department:")
            print("*"*40)  
            for dept, count in student_frequency.items():
                 print(f" 👉 {count} students in {dept} department.")
    
    menu()
        


# 13. function to display all information in the file system 
def show_all():
    print("\n\tAll Student Information:")
    print("*"*43)
    with open("student_db.txt", 'r') as file:
        found = False       
        for line in file:
            try:# handle the file format error(how the file is formatted?)
               stid,name,gender,dep,gpa = line.split(";")
               print(f" ID: {stid}\n Name: {name}\n Gender: {gender}\n Department: {dep}\n GPA: {gpa}\n")
               found =True 
            except ValueError:
                continue 
        if not found:
            print("  😵 Sorry! The file is empty.")        
        print("*"*43)
    menu()


                     
                     
# 14. function to delete all information from the system              
def delete_all_data():
    with open("student_db.txt", "w") as file:
        file.write("")
    print("All data deleted successfully.")
    show_all()
    menu()    
  
    
 # 0. function to exit the system 
def Exit():
    exit("👉 Thank you,the the system is exited.")
    
    
 # function used as main method to tell the menu as main method to be used the system 
if __name__ == "__main__":
    menu()
    
    