#Thil is testing commit
# This file will have the program class
import csv
import re
from Course import Course #random comment

class ProgramDoesNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg
class ProgramAlreadyExists(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class Program:
    def __init__(self,program_code,program_name,program_year,program_core,program_elec,program_credits):
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

    def set_p_year(self, year=''):
        self.p_year = year
    def get_year(self):
        return self.p_year

    def set_p_core(self, core=''):
        self.p_core = core
    def get_pre(self):
        return self.p_core

    def set_p_elec(self, electives=''):
        self.p_elect = electives
    def get_p_elec(self):
        return self.p_elec

    def set_p_creds(self, credits=''):
        self.p_credits = credits
    def get_p_creds(self):
        return self.p_credits
    
    def __str__(self):
        string = ''
        string += 'Program Code: '+ self.get_code() + '\nProgram Name: ' + self.get_name() 
        string += '\nTotal Credits: '+ self.get_p_creds() + '\n'
        string += '\n' + self.get_year() + '\nCore Coures: ' + '\n'
        for i in self.p_core.split(','):
            string += i + '\t'
        
        string += '\n\nElectives: '+ '\n'
        for i in self.p_elec.split(','):
            string += i + '\t'
        string += '\n'
        string += '\n--------------------------------------'
        return string
    

#answer = input('Which course plan would you like to view?')
#add and remove program for admin 

    def print_all_program_info(self):
        with open('bp096_1.csv', 'r') as csv_se:
            reader = csv.reader(csv_se, delimiter=',')
            
            copy_list = [] 
            for row in reader:
                if row != '':
                    copy_list.append(row)

            info_string = ''
            info_string += "Program Code = " + copy_list[1][0] + '\n'
            info_string += "Program Name = " + copy_list[1][1] + '\n'
            info_string += "Total Credits = " + copy_list[6][1] +'\n\n'
       
        with open('bp094.csv', 'r') as csv_se:
            reader = csv.reader(csv_se, delimiter=',')

            copy_list2 = [] 
            for row in reader:
                if row != '':
                    copy_list2.append(row)
            
            info_string += "Program Code = " + copy_list2[1][0] + '\n'
            info_string += "Program Name = " + copy_list2[1][1] + '\n'
            info_string += "Total Credits = " + copy_list2[5][1]

        return info_string

    def delete_program(self, unwanted_program):

        se_program = self.print_program_info('bp096_1.csv')
        se_list = list(se_program.split(" "))
        cs_program = self.print_program_info('bp094.csv')
        cs_list = list(cs_program.split(" "))
        
        all_list = []
        all_list.append(se_list)
        all_list.append(cs_list)

        try:
            if unwanted_program == 'BP094' or unwanted_program == 'bp094':
                all_list.pop(0)
                return print(f'Bachelor of Computer Science successfully removed.\n\nRemaining Program:\n\n{se_program}')
            
            elif unwanted_program == 'bp096' or unwanted_program =='BP096':
                all_list.pop(1)
                return print(f'Bachelor of Software Engineering successfully removed.\nRemaining Program:\n\n{cs_program}')
            else:
                raise ProgramDoesNotExist('This program does not exist.\nPlease enter existing program.')
        except ProgramDoesNotExist as error:
            print(error.mssg)

    def add_program(self, new_code,new_program,new_credit):
        programs = self.print_all_program_info()
        programs_list = list(programs.split(" "))

        try:
            if new_code == 'BP094' or new_code == 'bp094' or new_program.casefold() == 'bachelor of computer science':
                raise ProgramAlreadyExists('This program already exists.\nPlease enter new program.')
            
            elif new_code == 'bp096' or new_code =='BP096' or new_program.casefold() == 'bachelor of software engineering':
                raise ProgramAlreadyExists('This program already exists.\nPlease enter new program.')
            else:
                info_string = ''
                info_string += "Program Code = " + new_code + '\n'
                info_string += "Program Name = " + new_program + '\n'
                info_string += "Total Credits = " + new_credit

                info_list = list(info_string.split(" "))
                all_list.append(info_list)

                print(f'Succefully added {new_program}!' )
                print('')

        except ProgramAlreadyExists as error:
            print(error.mssg)
        return  programs_list

    

    def load_program_objects(self, filename): #
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)
            program_list =[]
            if filename == 'bp096_1.csv':
                program_code = list_of_csv[1][0]
                program_name = list_of_csv[1][1]
                program_elec = list_of_csv[5][3]
                program_credits = list_of_csv[6][1]
            
            elif filename == 'bp094.csv':
                program_code = list_of_csv[1][0]
                program_name = list_of_csv[1][1]
                program_elec = list_of_csv[4][3]
                program_credits = list_of_csv[5][1]

            for x in range(1,len(list_of_csv)):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                if program_year == 'Elective Courses' or program_year == 'Top 5 Electives':
                    pass
                elif program_year == 'Year 1':
                    program_object = Program(program_code,program_name,program_year,program_core,'No Electives',program_credits)
                    program_list.append(program_object)
                else:
                    program_object = Program(program_code,program_name,program_year,program_core,program_elec,program_credits)
                    program_list.append(program_object)
            
            return program_list
    

    def easy_courses(self): #Displays the top ten easy courses for each program - Julia Phan
        with open('bp094.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            copy_list = [] 
            for row in reader:
                if row != '':
                    copy_list.append(row)
            course_list1 = copy_list
            courses_samp1 = [course_list1[i][3] for i in range(len(course_list1)-1)]
            courses_samp1.pop(0)

        cs_list = []
        for course in courses_samp1:
            for i in course.split(','):
                cs_list.append(i)
    
        with open('bp096_1.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            copy_list = [] 
            for row in reader:
                if row != '':
                    copy_list.append(row)
            cs_courses = copy_list
            courses_samp = [cs_courses[i][3] for i in range(len(cs_courses)-1)]
            courses_samp.pop(0)

        se_list = []
        for course in courses_samp:
            for i in course.split(','):
                se_list.append(i)

        cs_w_rankings = dict()
        se_w_rankings = dict()
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            for info in list_of_csv:
                code = info[0]
                rank = int(info[8])
                for cs in cs_list:
                    if cs== code:
                        cs_w_rankings[code] = rank
                for se in se_list:
                    if se== code:
                        se_w_rankings[code] = rank

        sorted_cs = list(cs_w_rankings.items())
        for mx in range(len(sorted_cs)-1, -1, -1):
            swapped = False
            for i in range(mx):
                if sorted_cs[i][1] < sorted_cs[i+1][1]:
                    sorted_cs[i], sorted_cs[i+1] = sorted_cs[i+1], sorted_cs[i]
                    swapped = True
            if not swapped:
                break

        sorted_se = list(se_w_rankings.items())
        for mx in range(len(sorted_se)-1, -1, -1):
            swapped = False
            for i in range(mx):
                if sorted_se[i][1] < sorted_se[i+1][1]:
                    sorted_se[i], sorted_se[i+1] = sorted_se[i+1], sorted_se[i]
                    swapped = True
            if not swapped:
                break
    
        last_cs_courses = sorted_cs[:10] #first ten elements since
        last_se_courses = sorted_se[:10] #sorted in descending order
    
        new_cs = [new[0] for new in last_cs_courses]
        new_se = [new[0] for new in last_se_courses]

        del last_cs_courses
        del last_se_courses

        '''
        CS
        ['COSC1147', 'COSC2802', 'MATH2412', 'COSC2276', 'COSC2408', 
        'COSC2673', 'COSC1107', 'ISYS1118', 'COSC2299', 'COSC1076']
        SE
        ['COSC1226', 'ISYS1126', 'COSC1147', 'COSC2802', 'ISYS2405', 
        'MATH2412', 'INTE2376', 'COSC2799', 'COSC1183', 'COSC2471']
        '''
        
        
        print('Which Program\'s Top 10 Easiest Courses would you like to view?')
        print('Bachelor of Computer Science (BP094)     ||      Bachelor of Software Engineering (BP096)')
        prog_code = input('Please enter a Program\'s code: ')
        while True:
            if prog_code == 'BP094' or prog_code == 'bp094':
                print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
                print('                                               ')
                print('    Top 10 Easiest Computer Science Courses    ')
                print('                                               ')
                print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
                with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=',')
                    headings = next(csv_reader)
                    list_of_csv = list(csv_reader)
                    cs_courses = []
                    for info in list_of_csv:
                        course_code = info[0]
                        course_name = info[1]
                        desc = info[2]
                        credit_points = int(info[4])
                        prereq = info[3]
                        ava_sem = info[5]
                        for new in new_cs:
                            if new == course_code:
                                course_object = Course(course_name, course_code, desc, credit_points, prereq, ava_sem)
                                cs_courses.append(course_object)     
                cs_courses[0].__str__()
                break
            elif prog_code == 'BP096' or prog_code == 'bp096':
                print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
                print('                                               ')
                print('  Top 10 Easiest Software Engineering Courses  ')
                print('                                               ')
                print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
                with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=',')
                    headings = next(csv_reader)
                    list_of_csv = list(csv_reader)
                    se_courses = []
                    for info in list_of_csv:
                        course_code = info[0]
                        course_name = info[1]
                        desc = info[2]
                        credit_points = int(info[4])
                        prereq = info[3]
                        ava_sem = info[5]
                        for new in new_se:
                            if new == course_code:
                                course_object = Course(course_name, course_code, desc, credit_points, prereq, ava_sem)
                                se_courses.append(course_object) 
                se_courses[0].__str__()
                break
            else:
                print('Invalid Program Code! Please try again!')
                prog_code = input('Please enter a Program\'s code: ')
    
    def load_popElects(self): # Extended feature by Mihika (Popular Electives)
        print('Enter Program Code to see list of popular electives:')
        progCode = input()
        if progCode == 'BP094':
            with open('bp094.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                csv_list = list(csv_reader)
                popElects = csv_list[5][3].split(',')
                pp_lects = []
                for pop in popElects:
                    pp_lects.append(pop)
                print('Top 5 Electives in Computer Science:')
                for pps in pp_lects:
                    Course.SearchCourse(self, pps)
        elif progCode == 'BP096':
            with open('bp096_1.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                csv_list = list(csv_reader)
                popElects = csv_list[6][3].split(',')
                pp_lects = []
                for pop in popElects:
                    pp_lects.append(pop)
                print('Top 5 Electives in Software Engineering:')
                for pps in pp_lects:
                    Course.SearchCourse(self, pps)
        else:
            raise ProgramDoesNotExist('Program Does Not Exist')                        

se_program = Program('c','c','c','c','c','c')


#printing all info for each program
#print(se_program.print_program_info('bp094.csv'))
programs = se_program.load_program_objects('bp094.csv')
for program in programs:
    print(program)
    print('')

programs = se_program.load_program_objects('bp096_1.csv')
for program in programs:
    print(program)
    print('')




'''''

electives = se_program.load_program_electives('bp094.csv')
print('List of Electives:')
for elective in electives:
    print(elective + ', ')

'''''
#se_program.load_popElects() testing Popular Electives Extended Feature

'''''
new_list = se_program.print_all_program_info()
better_list = re.split(':|=|; |, |\n',new_list)
print(new_list)
#print('')
#print(se_program.print_program_info('bp096_1.csv'))

'''''


testing = se_program.add_program('B096','Bachelor of Computer Science','dsd')
for program in testing:
    print(' '.join(program))
    print('')


#print(se_program.easy_courses())







    





