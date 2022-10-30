
# This will be the main menu of our Enrolement System
from fileinput import filename
from re import U
from Course import Course
from Program import Program, Program_by_year
from Semester import Semester, Load_data, CourseOffering 
from Student import Student, Student_list
import math
import sys
import csv

class InvLoginOption(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

    def __str__(self):
        print(self.mssg)

class StudentNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

    def __str__(self):
        print(self.mssg)

class AdminNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

    def __str__(self):
        print(self.mssg)       

class OptionNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

    def __str__(self):
        print(self.mssg)    

class StudentAlreadyExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

    def __str__(self):
        print(self.mssg)

class StuLogin(Student):
    def __init__(self,snum, sname):
        self.snum = snum
        self.sname = sname
        Student.load_students()
        self.StuList = Student_list
        self.AcadHist = ''
        self.curr_enrol = ''
        self.studplan = ''

    def print_login_info(self):
        #StuList = Student.load_students()
        for Stud in self.StuList:
            if self.snum in Stud:
                print(f'Welcome {self.sname}', end = ' ')
                print(f'\tStudent ID Number: {self.snum}')
                print(f'D.O.B: {Stud[2]}', end = ' ')
                print(f'\tProgram Code : {Stud[3]}')
                self.AcadHist = Stud[4]
                print('Courses Currently Enrolled in:')
                self.curr_enrol = Stud[5]
                enrol_str = ''
                for curr in self.curr_enrol.split(','):
                    for j in curr:
                        enrol_str += j.strip()
                    enrol_str += ' '
                print(enrol_str)
                self.studplan = Stud[6] 
                break   
        else:
            raise StudentNotExist('Student Does Not Exist in list.')  

    def display(self, usr_inp):
        if usr_inp == 'C':
            Course.__str__(self)
        elif usr_inp == 'SEM':
            inpY = input('Enter Year: Y1/Y2\n')
            inpS = input('Enter Semester: S1/S2\n')
            print(Semester(inpS, inpY))   
        elif usr_inp == 'S':
            print('Enter course code to search:')
            cr_code = input().upper()
            Course.SearchCourse(self,cr_code)
        elif usr_inp == 'E':
            Program_by_year.easy_courses(self)
        elif usr_inp == 'D':
            Program_by_year.hard_courses(self)
        elif usr_inp == 'SC':
            search_number = input('\nEnter Student Number to Access Your Credits: ')
            print(Student.load_student_credit(search_number))
        elif usr_inp == 'PE':
            Program_by_year.load_popElects(self)
        elif usr_inp == 'R':
            print('To Enrol in a course, type ADD')
            print('To Unenrol in from a course, press REM')
            inp = input().upper()
            if inp == 'ADD':
                cr_code = input('Enter course code\n')
                sem = input('Enter Current Semester: Y1 or Y2\n')
                yrs = input('Enter Year of Current Enrollment:\n')
                self.curr_enrol = Student.ammend_current_enrollment_add(self, yrs, sem, cr_code, self.curr_enrol)
                print('Updated Current Enrolment')
                print(self.curr_enrol)
            elif inp == 'REM':
                cr_code = input('Enter course code\n')
                sem = input('Enter Semester: Y1 or Y2\n')
                Student.ammend_current_enrollment_remove(self, sem, cr_code) 
        else:
            raise OptionNotExist('Chosen Option does not exist')

#########################################
#Admin menu class starts here
class Admin(Student):
    def __init__(self, adm_num, adm_nm):
        self.admin_num = adm_num
        self.admin_name = adm_nm
        self.adm_dict = {}
        Student.load_students()
        self.StuList = Student_list

    def load_admin_list(self, filename = 'Admin.csv'):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',') 
            headings = next(csv_reader)
            adms = list(csv_reader)
            for adm in adms:
               self.adm_dict[adm[0]] = adm[1]
            #return self.adm_list                  

    def print_info(self):
        Admin.load_admin_list(self)
        if self.admin_num in self.adm_dict.keys():
            print('Welcome Admin')
            print(f'Admin Number: {self.admin_name}', end = ' ')
            print(f'\tAdmin Name: {self.admin_num}')
        else:
            raise AdminNotExist('Admin does not exist')
            #sys.exit('Logged Out as Admin does not exist')

    def display(self, usr_inp):
        if usr_inp == 'D': # Display student list
            for stud in self.StuList:
                String = ''
                String += 'Name: ' + stud[0]
                String += '\nStudent ID: ' + stud[1]
                String += '\nDate of birth: ' + stud[2]
                String += '\nCurrently enrolled program: ' + stud[3]
                String += '\nAcademic History: ' 
                for i in stud[4].split('!'):
                    String += '\n'
                    i.strip()
                    for j in i.split(','):
                        String += j.strip() + ' '
                String += '\nCurrent enrollment: \n'
                for i in stud[5].split(','):
                    for j in i:
                        String += j.strip()
                    String += ' '
                String += '\nStudy plan: '
                for i in stud[6].split('!'):
                    String += '\n'
                    for j in i.split(','):
                        String += j.strip() + ' '
                print(String)        
        elif usr_inp == 'ALL': #Display all programs
            for program in Program_by_year.load_program_objects(self):
                print(program)
        elif usr_inp == 'AP': #Add a program
            print('Please fill in the required attributes to add new program')
            p_code = input('Enter Program Code: \n')
            p_name = input('Enter Program Name: \n')
            p_year = input('Enter duration of the Program: \n')
            p_core = input('Enter Core Courses with , to Seperate Each Courses: \n')
            p_electives = input('Enter Elective Courses with , to Seperate Each Courses: \n')
            p_credit = input('Enter Required Credits to Graduate: \n')

            new_program = Program_by_year(p_code,p_name,p_year,p_core,p_electives,p_credit)
            new_prog = Program(p_code,p_name,p_credit)
            add_program = new_prog.add_program(new_program)
            for program in add_program:
                print(program)
            print(f'Successfully added {new_program.get_name()}!\n')

        elif usr_inp == 'RP': #Remove program
            p_code = input('Please Enter the Program Code to Delete (bp094) or (bp096): \n')
            #There is only two program objects in the default program list so it can 
            #only remove either 'BP094' or 'BP096'
            program_object = Program()
            for program in Program_by_year.load_program_objects(self):
                if p_code == program.get_code().casefold():
                    program_name = program.get_name()
                    delete_program = program_object.delete_program(program)
                else:
                    pass
            for program in delete_program:
                print(program)
            print(f'Successfully removed {program_name}!\n')

        elif usr_inp == 'AS': #Add a student in StuList
            s_name = input('Enter Student Name:\n')
            for stud in self.StuList:
                if s_name == stud[0]:
                    raise StudentAlreadyExist('Student already in Student Roster')
            s_id = input('Enter Student ID Number:\n')
            s_DOB = input('Enter Student Date of Birth in DD-MM-YYYY format:\n')  
            s_progcode = input('Enter Student\'s Program code:\n')
            s_acadhist = input('Enter Student\'s Academic History[Eg.: "Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235" or NULL]:\n')
            s_currenrol = input('Enter Student\'s Current Enrolment[Eg.: "Y1,S1,COSC1234,MATH1234,COSC4321"]:\n') 
            s_stuplan = input('Enter Student\'s Study Plan[Eg.: "Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235" or NULL]') 
            Student([s_name, s_id, s_DOB, s_progcode, s_acadhist, s_currenrol, s_stuplan])    
        elif usr_inp == 'ASC': #Add Student in a course
            inpName = input('Enter Student Name: \n')
            inpSno = input('Enter Student ID: E.g. s123456\n')
            inpDOB = input('Enter Date of Birth: dd-mm-yyyy\n')
            inpPCode = input('Enter Program Code: \n')
            inpAca = input('Enter Academic History: E.g."Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235" or NULL\n')
            inpCur = input('Enter Current Enrolment: E.g."Y1,S1,COSC1234,MATH1234,COSC4321"\n')
            inpStu = input('Enter Study Plan: E.g. "Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235" or NULL\n')
            student1 = Student(inpName, inpSno, inpDOB, inpPCode, inpAca, inpCur, inpStu)
            inpCcode = input('Enter Course Code: \n')
            inpCname = input('Enter Corresponding Course Name: \n')
            inpYear = input('Enter Year: Y1/Y2\n')
            inpSem = input('Enter Semester: S1/S2\n')
            inpMax = input('Enter Maximum No. Students: \n')
            courseoffer1 = CourseOffering(inpCcode, inpCname, inpYear, inpSem, inpMax)
            courseoffer1.add_student(student1)
            print(courseoffer1)
        elif usr_inp == 'RS': #Remove student from StuList
            inpStuName = input('Enter Student Name to remove:\n')
            for stud in self.StuList:
                if inpStuName == stud[0]:
                    self.StuList.remove(stud)
        elif usr_inp == 'RSC': #Remove student from course
            inpSno = input('Enter Student ID: E.g. s123456\n')
            inpCcode = input('Enter Course Code: \n')
            inpCname = input('Enter Corresponding Course Name: \n')
            inpYear = input('Enter Year: Y1/Y2\n')
            inpSem = input('Enter Semester: S1/S2\n')
            inpMax = input('Enter Maximum No. Students: E.g. 250 or 4\n')
            courseoffer1 = CourseOffering(inpCcode, inpCname, inpYear, inpSem, inpMax)
            courseoffer1.remove_student(inpSno)
            print(courseoffer1)
        elif usr_inp == 'ASP': #Amend Study Plan
            print('Please fill in the required attributes for the student')
            s_name = input('Enter Student Name: \n')
            s_student_ID = input('Enter Student ID: \n')
            s_DOB = input('Enter D.O.B \n')
            s_program_code = input('Enter Program Code: \n')
            s_academic_history = input('Enter Academic History: \n')
            s_current_enrollment = input('Enter Current Enrollment: \n')
            s_study_plan = input('Enter Study Plan: \n')

            new_student = Student(s_name, s_student_ID, s_DOB, s_program_code, s_academic_history, s_current_enrollment, s_study_plan)

            A_or_R = input('Would you like to add or remove a course from study plan?\n Enter A for add and R for Remove.\n')
            if A_or_R == 'A':
                print('Please fill in the required attributes to amend your study plan')
                s_year = input('Enter Year: \n')
                s_sem = input('Enter Semester: \n')
                s_course = input('Enter Course to add: \n')

                new_student.ammend_study_plan_add(s_year, s_sem, s_course)

            elif A_or_R == 'R':
                print('Please fill in the required attributes to amend your study plan')
                s_year = input('Enter Year: \n')
                s_sem = input('Enter Semester: \n')
                s_course = input('Enter Course to remove: \n')

                new_student.ammend_study_plan_remove(s_year, s_sem, s_course)

        elif usr_inp == 'AAH': #Amend Academic History
            print('Please fill in the required attributes for the student')
            s_name = input('Enter Student Name: \n')
            s_student_ID = input('Enter Student ID: \n')
            s_DOB = input('Enter D.O.B \n')
            s_program_code = input('Enter Program Code: \n')
            s_academic_history = input('Enter Academic History: \n')
            s_current_enrollment = input('Enter Current Enrollment: \n')
            s_study_plan = input('Enter Study Plan: \n')

            new_student = Student(s_name, s_student_ID, s_DOB, s_program_code, s_academic_history, s_current_enrollment, s_study_plan)

            print('Please fill in the required attributes to amend your academic history.')
            s_course = input('Enter Course to ammend: \n')
            s_mark = input('Enter Mark: \n')
            s_grade = input('Enter Grade: \n')

            new_student.ammend_academic_history(s_course, s_mark, s_grade)
        elif usr_inp == 'AC': #Add course
            c_code = input('Enter code of new course[Eg.: COSC2555 or ISYS1212]:\n')
            c_title = input('Enter name of new course:\n')
            c_desc = input('Enter a description of new course:\n')
            c_creds = input('Enter total credit points of new course:\n')
            c_prereq = input('Enter prerequisites of new course[Eg.: "COSC2555,ISYS1122" or NULL]:\n')
            c_sem = input('Enter available semesters of new course[Eg. "Y1,Y2" or Y1 or Y2]:\n')
            c_gdis = "HD:80-100,DI:70-79,CR:60-69,PA:50-59,NN:0-49"
            Course.addCourse(self, c_code, c_title, c_desc, c_creds, c_prereq, c_sem, c_gdis)
        else:
            raise OptionNotExist('Chosen Option does not exist') 


#################################################################

print('===============================================')
print('          WELCOME TO ENROLMENT ONLINE          ')
print('===============================================')

##adm1 = Admin()
print('To Login as Student, type S')
print('To Login as Admin, type A')
logtype=input().upper()
if logtype == 'S':
    ##Something to redirect student to Student class
    print('Enter Student Number:')
    snumb = input()
    print('Enter Student Name:')
    sname = input()
    Stu1 = StuLogin(snumb,sname)
    Stu1.print_login_info()
    print('===============Main Menu===============')
    print('To See List of Courses, type C')
    print('To See a List of Courses by Semester, type SEM')
    print('To Search a Courses, type S')
    print('To See List of Easiest Courses, type E')
    print('To See List of Most Difficult Courses, type D')
    print('To See your Remaining Course Credits, type SC')
    print('To See List of Popular Electives, type PE')
    print('To Enrol/Unenrol from Program, type R')
    print('To Exit, type Q')
    usrinp = input().upper()
    while usrinp != 'Q':
        Stu1.display(usrinp)
        print('===============Main Menu===============')
        print('To See List of Courses, type C')
        print('To See a List of Courses by Semester, type SEM')
        print('To Search a Courses, type S')
        print('To See List of Easiest Courses, type E')
        print('To See List of Most Difficult Courses, type D')
        print('To See your Remaining Course Credits, type SC')
        print('To See List of Popular Electives, type PE')
        print('To Enrol/Unenrol from Program, type R')
        print('To Exit, type Q')
        usrinp = input().upper()
elif logtype == 'A':
    ##Redirects to Admin class 
    print('Enter Admin Number')
    adm = input()
    print('Enter Admin Name')
    adm_name = input()
    adm1 = Admin(adm, adm_name)
    adm1.print_info()   
    print('===============Main Menu===============')
    print('To see List of Students, type D')
    print('To See List of All Programs, type ALL')
    print('To Add a Program, type AP')
    print('To Remove a Program, type RP')
    print('To Add Student in Student List, type AS')
    print('To Add Student in a Course, type ASC')
    print('To Remove Student from Student List, type RS')
    print('To Remove Student from Course, type RSC')
    print('To Amend Study Plan, type ASP')
    print('To Amend Academic History, type AAH')
    print('To Add Course, type AC')
    print('To Exit, type Q')
    usrinp = input().upper()

    while usrinp != 'Q':
        adm1.display(usrinp)
        print('===============Main Menu===============')
        print('To see List of Students, type D')
        print('To See List of All Programs, type ALL')
        print('To Add a Program, type AP')
        print('To Remove a Program, type RP')
        print('To Add Student in Student List, type AS')
        print('To Add Student in a Course, type ASC')
        print('To Remove Student from Student List, type RS')
        print('To Remove Student from Course, type RSC')
        print('To Amend Study Plan, type ASP')
        print('To Amend Academic History, type AAH')
        print('To Add Course, type AC')
        print('To Exit, type Q')
        usrinp = input().upper()
else:
    raise InvLoginOption('Invalid Login Option. Restart to Login again')



'''def main():
    Student_list'''






sys.exit('Log Out Successful')








