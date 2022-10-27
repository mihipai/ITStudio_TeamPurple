#Kelvin Duong Ly, s3953996
# This file will have the student class
from os import remove
from turtle import st
import csv

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
        String = 'Your Current Enrollment:'
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
        for i in self.study_plan.split('!'):
            String += '\n'
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
        self.academic_history = '!'.join(split)
        return print('Academic History has been successfully ammended.')
    
    def ammend_study_plan(self, year, sem, remove_from_study_plan):
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
        self.study_plan = '!'.join(split)

        return print('Study Plan has been successfully ammended.')
    
    def load_students(self):
        with open('Students.csv', 'r', encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            student_list = []

            for i in range(len(list_of_csv)):
                name =  list_of_csv[i][1]
                student_id = list_of_csv[i][0]
                dob = list_of_csv[i][3]
                program_code = list_of_csv[i][4]
                academic_history = list_of_csv[i][7]
                current_enrollment = list_of_csv[i][5]
                study_plan = list_of_csv[i][6]
                Student_object = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
                student_list.append(Student_object)
        return student_list

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
student1.ammend_study_plan('Y1', 'S2', 'MATH2412')
student1.print_study_plan()
student1.ammend_study_plan('Y1', 'S2', 'COSC2802')
student1.ammend_study_plan('Y1', 'S2', 'COSC2804')
student1.print_study_plan()