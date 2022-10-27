#Thil is testing commit
# This file will have the program class
import csv

class InvProgName(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class Program:
    def _init_(self,program_code,program_name,program_year,program_core,program_elec,program_credits):
        self.p_code = program_code
        self.p_name = program_name
        self.p_year = program_year
        self.p_core = program_core
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

    def set_p_core(self, core=''):
        self.p_core = core
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

#answer = input('Which course plan would you like to view?')

#if answer == 'BP096' or 'bp096':
    def load_welcome_page(self):
        print('')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('')
        print('Welcome to Bachelor of Software Engineering!')
        print('')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('')

    def load_program(self, file_name):
        with open(file_name, 'r') as csv_se:
            reader = csv.reader(csv_se, delimiter=',')
            
            copy_list = [] 

            for row in reader:
                if row != '':
                    copy_list.append(row)
            
            self.p_code = copy_list[2][0]
            self.p_name = copy_list[2][1]
            
            #copies list from copy_list into year_list
            year_list = copy_list

            #years list is used to make adjustments from the csv
            #such as removing program code and name so it's not repetitive
            
            years=[]
            for i in range(len(year_list)):
                years.append(year_list[i][2])
            years.pop(0)

            if file_name == 'bp096_1.csv':
                self.p_credits = year_list[6][1]
                years.pop(5)
            elif file_name == 'bp094.csv':
                self.p_credits = year_list[5][1]
                years.pop(4)

            #copies list from copy_list into course_list
            course_list = copy_list
            courses = []
            for i in range(len(course_list)-1):
                courses.append(course_list[i][3])
            courses.pop(0)
            courses_dict = dict(zip(years, courses))

            print('')
            print('Program Code: ' + self.p_code)
            print('Program Name: ' + self.p_name)
            print('Program Total Credits: ' + self.p_credits)
            print('')

            for key,value in courses_dict.items():
                print(key + ' : ' + value)
                print('')
            
    
    def easy_courses():
        with open('BP094.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            copy_list = []
            for row in list_of_csv:
                if row != '':
                    copy_list.append(row)

            cs_str = ''
            computer_science = copy_list
            cs_row = computer_science[5]
            cs_str += cs_row[3]
            comp_longlist = cs_str.split(',')

        with open('BP096.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            copy_list = []
            for row in list_of_csv:
                if row != '':
                    copy_list.append(row)

            se_str = ''
            software_engineer = copy_list
            se_row = software_engineer[6]
            se_str += se_row[3]
            soft_longlist = se_str.split(',')

        print('Which program\'s list of easiest courses would you like to view?')
        print('Bachelor of Computer Science (BP094)         ||          Bachelor of Software Engineering (BP096)')
        prog_name = input('Please enter a Program\'s code: ')
        print()
        while True:
            try:
                if prog_name == 'BP094' or prog_name == 'bp094':
                    with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
                        csv_reader = csv.reader(csvfile, delimiter=',')
                        headings = next(csv_reader)
                        list_of_csv = list(csv_reader)
                        computer_courses = []
                        for info in list_of_csv:
                            code = info[0]
                            name = info[1]
                            credits = info[4]
                            prereq = info[3]
                            ava_sem = info[5]
                            for comp in comp_longlist:
                                if comp == code:
                                    course_object = Course(code,name,credits,prereq,ava_sem)
                                    computer_courses.append(course_object)
                    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
                    print('                                               ')
                    print('    List of Easiest Computer Science Courses   ')
                    print('                                               ')
                    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
                    print(computer_courses[0])
                    break

                elif prog_name == 'BP096' or prog_name == 'bp096':
                    with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
                        csv_reader = csv.reader(csvfile, delimiter=',')
                        headings = next(csv_reader)
                        list_of_csv = list(csv_reader)
                        software_courses = []
                        for info in list_of_csv:
                            code = info[0]
                            name = info[1]
                            credits = info[4]
                            prereq = info[3]
                            ava_sem = info[5]
                            for soft in soft_longlist:
                                if soft == code:
                                    course_object = Course(code,name,credits,prereq,ava_sem)
                                    software_courses.append(course_object)
                    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
                    print('                                                   ')
                    print('    List of Easiest Software Engineering Courses   ')
                    print('                                                   ')
                    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
                    print(software_courses[0])
                    break
                else:
                    raise InvProgName('Invalid Program Option! Please try again.')
            except InvProgName as error:
                print(error.mssg)
                prog_name = input('Please enter a Program\'s code: ')

#else:
    #print('goodbye')

se_program = Program()
se_program.set_p_code()
se_program.set_p_name()
se_program.set_p_core('Math')
se_program.set_p_elec('English')
se_program.set_p_creds('9')
#se_program.print_program_info()
se_program.load_program('bp094.csv')


    





