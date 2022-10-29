
# This will be the main menu of our Enrolement System
from fileinput import filename
from Course import Course
from Program import Program
from Semester import Semester
from Student import Student
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


class StuLogin:
    def __init__(self,snum, sname):
        self.snum = snum
        self.sname = sname
        self.StuList = Student.load_students()

    def print_login_info(self):
        if self.snum in self.StuList and self.sname in self.StuList:
            print(f'Welcome {self.sname}', end = ' ')
            print(f'\tStudent Number: {self.snum}')
            print(f'D.O.B: {self.getDOB()}', end = ' ')
            print(f'Program Code : {self.get_program_code()}')
            print('Courses Currently Enrolled in:')
            curr_enrol = self.get_current_enrollment()
            enrol_str = ''
            for i in self.current_enrollment.split(','):
                for j in i:
                   enrol_str += j.strip()
                enrol_str += ' '
            print(enrol_str)
        else:
            raise StudentNotExist('Student Does Not Exist in list.')
            #sys.exit('Student Does not exist')  

    def display(self, usr_inp):
        if usr_inp == 'C':
            print(Course.__str__())
        elif usr_inp == 'S':
            print('Enter course code to search:')
            cr_code = input().upper()
            Course.SearchCourse(cr_code)
        elif usr_inp == 'E':
            Program.easy_courses()
        elif usr_inp == 'D':
            pass
        elif usr_inp == 'PE':
            Program.load_popElects()
        elif usr_inp == 'R':
            print('To Enrol in a course, type ADD')
            print('To Unenrol in from a course, press REM')
            inp = input().upper()
            if inp == 'ADD':
                cr_code = input('Enter course code\n')
                sem = input('Enter Current Semester: Y1 or Y2\n')
                yrs = input('Enter Year of Current Enrollment:\n')
                Student.ammend_current_enrollment_add(yrs, sem, cr_code)
            elif inp == 'REM':
                cr_code = input('Enter course code\n')
                sem = input('Enter Semester: Y1 or Y2\n')
                Student.ammend_current_enrollment_remove(sem, cr_code) 
        else:
            raise OptionNotExist('Chosen Option does not exist')

#########################################
#Admin menu class starts here
class Admin():

    def __init__(self, adm_num, adm_nm):
        self.admin_num = adm_num
        self.admin_name = adm_nm
        self.adm_dict = {}

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
        if usr_inp == 'D':
            pass
        elif usr_inp == '':
            pass


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
    print('To See List of Courses, type C')
    print('To See List of Courses, type C')
    print('To Search a Courses, type S')
    print('To See List of Easiest Courses, type E')
    print('To See List of Most Difficult Courses, type D')
    print('To See List of Popular Electives, type PE')
    print('To Enrol/Unenrol from Program, type R')
    print('To Exit, type Q')
    usrinp = input().upper()
    while usrinp != 'Q':
        Stu1.display(usrinp)
        print('To See List of Courses, type C')
        print('To Search a Courses, type S')
        print('To See List of Easiest Courses, type E')
        print('To See List of Most Difficult Courses, type D')
        print('To See List of Popular Electives, type PE')
        print('To Enrol/Unenrol from Program, type R')
        print('To Exit, type Q')
        usr_inp = input().upper()
elif logtype == 'A':
    ##Redirects to Admin class 
    print('Enter Admin Number')
    adm = input()
    print('Enter Admin Name')
    adm_name = input()
    adm1 = Admin(adm, adm_name)
    adm1.print_info()
    #usr_inp = input()
    #while usr_inp != 'Q':
    #    if usr_inp == 'D':
    #        print(Student)
else:
    raise InvLoginOption('Invalid Login Option. Restart to Login again')


sys.exit('Log Out Successful')








