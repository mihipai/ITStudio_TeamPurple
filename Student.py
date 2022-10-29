#Kelvin Duong Ly, s3953996
# This file will have the student class
Student_list = []
from os import remove
import csv

class StudentDoesNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class Student:
    #dunder init method
    def __init__(self, name, student_id, DOB, program_code, academic_history, current_enrollment, study_plan):
        self.name = name
        self.student_id = student_id
        self.DOB = DOB
        self.program_code = program_code
        self.academic_history = academic_history
        self.current_enrollment = current_enrollment
        self.study_plan = study_plan
        Student_list.append([name, student_id, DOB, program_code, academic_history, current_enrollment, study_plan])
#Setter, getter and print methods

    def set_name(self, name = ''):
        self.name = name
    def get_name(self):
        return self.name
    def print_name(self):
        print(f'Name: {self.name}')

    def set_student_id(self, student_id = ''):
        self.student_id = student_id
    def get_student_id(self):
        return self.student_id
    def print_student_id(self):
        print(f'Student ID: {self.student_id}')

    def set_DOB(self, DOB = ''):
        self.DOB = DOB
    def get_DOB(self):
        return self.DOB
    def print_DOB(self):
        print(f'Date of birth: {self.DOB}')
    
    def set_program_code(self, program_code = ''):
        self.program_code = program_code
    def get_program_code(self):
        return self.program_code
    def print_program_code(self):
        print(f'Currently enrolled program: {self.program_code}')
    
    def set_academic_history(self, academic_history = ''):
        self.academic_history = academic_history.strip()
    def get_academic_history(self):
        return self.academic_history
    def print_academic_history(self):
        String = 'Your academic history: '
        for i in self.academic_history.split('!'):
            String += '\n'
            i.strip()
            for j in i.split(','):
                String += j.strip() + ' '
        print(String)

    def set_current_enrollment(self, current_enrollment = ''):
        self.current_enrollment = current_enrollment.strip()
    def get_current_enrollment(self):
        return self.current_enrollment
    def print_current_enrollment(self):
        String = 'Your Current Enrollment:\n'
        for i in self.current_enrollment.split(','):
            for j in i:
                String += j.strip()
            String += ' '
        print(String)

    def set_study_plan(self, study_plan = ''):
        self.study_plan = study_plan.strip()
    def get_study_plan(self):
        return self.study_plan
    def print_study_plan(self):
        String = 'Your Study Plan:'
        self.study_plan.strip()
        for i in self.study_plan.split('!'):
            String += '\n'
            i.strip()
            for j in i.split(','):
                String += j.strip() + ' '
        print(String)

#dunder string method
    def __str__(self):
        String = ''
        String += 'Name: ' + self.name
        String += '\nStudent ID: ' + self.student_id
        String += '\nDate of birth: ' + self.DOB
        String += '\nCurrently enrolled program: ' + self.program_code
        String += '\nAcademic History: ' 
        for i in self.academic_history.split('!'):
            String += '\n'
            i.strip()
            for j in i.split(','):
                String += j.strip() + ' '
        String += '\nCurrent enrollment: \n'
        for i in self.current_enrollment.split(','):
            for j in i:
                String += j.strip()
            String += ' '
        String += '\nStudy plan: '
        for i in self.study_plan.split('!'):
            String += '\n'
            for j in i.split(','):
                String += j.strip() + ' '

        return String

    def ammend_academic_history(self, subject_to_ammend, mark, grade):
        split = self.academic_history.split('!')
        for i in range(len(split)):
            i_strip = split[i].strip()
            if i_strip == '':
                split.remove(split[i])
        for i in split:
            count = 0
            i_split = i.split(',')
            if subject_to_ammend in i_split[2]:
                i_split[3] = mark
                i_split[4] = grade
                split[count] = ','.join(i_split)
                count+=1
            else:
                return print('The course you are trying to ammend can not be found in academic history')
        self.academic_history = '!'.join(split)
        return print('Academic History has been successfully ammended.')
        
    def ammend_current_enrollment_remove(self, sem, remove_from_curr_enrollment):
        split = self.current_enrollment.split(',')
        if sem in split[1]:
            if remove_from_curr_enrollment in split:
                split.remove(remove_from_curr_enrollment)
                if len(split) == 2:
                    split = []
                else:
                    split_join = ''
                    for i in range(len(split)):
                        split_join = ','.join(split)
            else:
                return print('The course you want to remove can not be found in the current enrollment for the semester specified.')
        self.current_enrollment = split_join

        return print('Current Enrollment has been successfully ammended.')

    def ammend_current_enrollment_add(self, year, sem, add_to_curr_enrollment):
        split = self.current_enrollment.split(',')
        if year in split[0] and sem in split[1]:
            if add_to_curr_enrollment not in split:
                split.append(add_to_curr_enrollment)
                split_join = ''
                for i in range(len(split)):
                    split_join = ','.join(split)
            else:
                return print('That course already exists in Current Enrollment for that year and semester.')
        else:
            split_join = ''
            split_join += f'{year}, {sem}, {add_to_curr_enrollment}'
        self.current_enrollment = split_join
        return print('Current Enrollment has been successfully ammended.')
    
    def ammend_study_plan_remove(self, year, sem, remove_from_study_plan):
        split = self.study_plan.split('!')
        for i in split:
            count = 0
            split2 = i.split(',')
            if year in split2[0] and sem in split2[1]:
                for j in split2:
                    if remove_from_study_plan in j:
                        split2.remove(j)
                        if len(split2) == 2:
                            split.remove(i)
                        else:
                            split[count] = ','.join(split2)
                        count+=1
                    else:
                        return print('The course you want to remove can not be found in the study plan for the year and semester specified.')
        self.study_plan = '!'.join(split)
        return print('Study Plan has been successfully ammended.')

    def ammend_study_plan_add(self, year, sem, add_to_study_plan):
        split = self.study_plan.split('!')
        for i in split:
            count=0
            split2 = i.split(',')
            if year in split2[0] and sem in split2[1]:
                if add_to_study_plan not in split2:
                    split2.append(add_to_study_plan)
                    split_join = ''
                    for i in range(len(split2)):
                        split_join = ','.join(split2)   
                    split[count] = split_join
                    count+= 1
                else:
                    return print('That course already exists in Study Plan for that year and semester.')
            else:
                split_str = ''
                split_str += f'{year}, {sem}, {add_to_study_plan}'
                if split[-1][0] == None or split[-1][0] == ' ' or split[-1][0] == '':
                    split[-1] = split_str
            self.study_plan = '!'.join(split)
            return print('Study Plan has been successfully ammended.')
        self.study_plan = '!'.join(split)
        return print('Study Plan has been successfully ammended.')


    def load_students():
        with open('Students.csv', 'r', encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)

            for i in range(len(list_of_csv)):
                name =  list_of_csv[i][1]
                student_id = list_of_csv[i][0]
                dob = list_of_csv[i][3]
                program_code = list_of_csv[i][4]
                academic_history = list_of_csv[i][7]
                current_enrollment = list_of_csv[i][5]
                study_plan = list_of_csv[i][6]
                Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
    
    #Thilyka's extended feature:  Checking eligibility of graduation of a student, 
    #and print out detailed information about what is missing if not eligible. 

    def load_student_credit(search_number):

        #opens, reads and adds data into list of csv
        with open('Students.csv', 'r', encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            student_list = []

            #add data from list of csv into variables and arranges the elements in order of number
            #name,current credits,required credits and expected credits
            for i in range(len(list_of_csv)):
                student_number = list_of_csv[i][0]
                student_name = list_of_csv[i][1]
                student_current_credit = list_of_csv[i][9]
                student_required_credit = list_of_csv[i][10]
                student_expected_credit = list_of_csv[i][11]
                
                #info_string is a string of all the variables in order and use split to turn into a list so
                #it's easy to iterate
                info_string = student_number +" "+ student_name +" "+ student_current_credit +" "+ student_required_credit +" "+ student_expected_credit
                info_string = list(info_string.split(" "))
                student_list.append(info_string)
            
            #finding student based on their ID in the list and printing out their credit information 
            for student in student_list:
                for i in range(len(student)):
                    if search_number == student[i]:
                        info_string = ''
                        info_string += "Student ID = " + student[0] + '\n'
                        info_string += "Student Name = " + student[1] + ' ' + student[2] + '\n'
                        info_string += "Current Credits = " + student[3] + '\n'
                        info_string += "Required Credits = " + student[5] + '\n'
                        if int(student[4]) < 50:
                            info_string += 'Congratulations! You are graduating this year.'
                        else:
                            info_string += 'You are required to complete an overall amount of '+ student[4] +' credit points to graduate.'
                        return info_string
             
#Testing stuff# testing again
name = 'Kelvin'
student_id = 's3953996'
dob = '18/09/2001'
program_code = 'BP094GEN8'
academic_history = 'Y1,S1,COSC2801,89,HD ! Y1,S1,MATH2411,70,DI ! Y1,S1,COSC2803,63,CR ! Y1,S2,COSC2802,52,PA ! Y1,S2,MATH2412, 32, NN ! Y1,S2,COSC2804,55,PA ! '
current_enrollment = 'Y1,S1,COSC2801,MATH2411,COSC2803'
study_plan = 'Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235 ! Y2,S2,COSC1107,COSC1114,COSC2299,COSC2673 ! '
student1 = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
print(student1)
student1.ammend_academic_history('COSC2801', '80', 'HD')
student1.print_academic_history()
student1.ammend_study_plan_remove('Y1', 'S2', 'MATH2412')
student1.print_study_plan()
student1.ammend_study_plan_remove('Y1', 'S2', 'COSC2802')
student1.ammend_study_plan_remove('Y1', 'S2', 'COSC2804')
student1.print_study_plan()
Student.load_students()
student1.ammend_current_enrollment_remove('S1', 'COSC2801')
student1.print_current_enrollment()
student1.ammend_current_enrollment_add('Y1', 'S1', 'COSC2801')
student1.print_current_enrollment()
student1.ammend_current_enrollment_add('Y2', 'S1', 'COSC2123')
student1.print_current_enrollment()
student1.ammend_study_plan_add('Y2', 'S1', 'Testing')
student1.ammend_study_plan_add('Y3', 'S1', 'Testing')
student1.ammend_study_plan_add('Y2', 'S1', 'COSC2123')
student1.print_study_plan()
credits = Student.load_student_credit('s386570')

print(credits)