#Thil is testing commit
# This file will have the program class
import csv

class Program:
    def _init_(self,program_code,program_name,program_year,program_pre,program_elec,program_credits):
        self.p_code = program_code
        self.p_name = program_name
        self.p_year = program_year
        self.p_pre = program_pre
        self.p_elec = program_elec
        self.p_credits = program_credits
    
    def set_p_code(self, code =''):
        self.p_code = code
    def get_code(self):
        return self.p_code

    def set_p_name(self, name=''):
        self.p_name = name
    def get_name(self):
        return self.p_name

    def set_p_pre(self, prerequisites=''):
        self.p_pre = prerequisites
    def get_pre(self):
        return self.p_pre

    def set_p_elec(self, electives=''):
        self.p_elect = electives
    def get_p_elec(self):
        return self.p_elec

    def set_p_creds(self, credits=''):
        self.p_credits = credits
    def get_p_creds(self):
        return self.p_creds
    
    def print_program_info(self):
        print(f'Program Code: {self.p_code}\nProgram Name: {self.p_name}' )

print('')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
print('')
print('Welcome to Bachelor of Software Engineering!')
print('')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
print('')
    
answer = input('Which course plan would you like to view?')

if answer == 'BP096' or 'bp096':
    

    with open('bp096_1.csv', 'r') as csv_se:
        reader = csv.reader(csv_se, delimiter=',')
        
        copy_list = [] 
        for row in reader:
            if row != '':
                copy_list.append(row)
        
        #copies list from copy_list into year_list
        year_list = copy_list

        years=[]
        for i in range(len(year_list)):
            years.append(year_list[i][2])
        years.pop(0)
        years.pop(5)

        #copies list from copy_list into course_list
        course_list = copy_list
        courses = []
        for i in range(len(course_list)-1):
            courses.append(course_list[i][3])
        courses.pop(0)
        courses_dict = dict(zip(years, courses))

        for key,value in courses_dict.items():
            print(key + ' : ' + value)

else:
    print('goodbye')


'''''
se_program = Program()
se_program.set_p_code()
se_program.set_p_name()
se_program.set_p_pre('Math')
se_program.set_p_elec('English')
se_program.set_p_creds('9')
se_program.print_program_info()
'''''

    





