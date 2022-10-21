
# This will be the main menu of our Enrolement System
from Course import Course
from Program import Program
from Semester import Semester
from Student import Student
import math

class Admin():

    def __init__(self, adm_num):
        self.admin_num = adm_num

class InvLoginOption(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class StuLogin:
    def __init__(self,sname):
        self.sname = sname



print('===============================================')
print('          WELCOME TO ENROLMENT ONLINE          ')
print('===============================================')

##adm1 = Admin()
print('To Login as Student, type S')
print('To Login as Admin, type A')
logtype=input()
if logtype == 'S':
    ##Something to redirect student to Student class
    print('Enter Student Number:')
    snumb = input()
    Stu1 = StuLogin(snumb)
elif logtype == 'A':
    ##Redirects to Admin class 
    print('Enter Admin Number')
    adm = input()
    adm1 = Admin(adm)
else:
    raise InvLoginOption('Invalid Login Option. Restart to Login again')
       








