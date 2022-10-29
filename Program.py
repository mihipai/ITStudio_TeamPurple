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

#Program_by_year object loads each year of courses in the program into an object
class Program_by_year:
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
        return string

    #print program info with code,name,credit into strings, not useful in the end
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
   
    def load_program_objects(self): 
        with open('bp096_1.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)
            program_list =[]
            
            program_code = list_of_csv[1][0]
            program_name = list_of_csv[1][1]
            program_elec = list_of_csv[5][3]
            program_credits = list_of_csv[6][1]

            for x in range(1,len(list_of_csv)-2):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                if program_year == 'Elective Courses' or program_year == 'Top 5 Electives':
                    pass
                elif program_year == 'Year 1':
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,'No Electives',program_credits)
                    program_list.append(program_object)
                else:
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,program_elec,program_credits)
                    program_list.append(program_object)

        with open('bp094.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)

            program_code = list_of_csv[1][0]
            program_name = list_of_csv[1][1]
            program_elec = list_of_csv[4][3]
            program_credits = list_of_csv[5][1]

            for x in range(1,len(list_of_csv)-2):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                if program_year == 'Elective Courses' or program_year == 'Top 5 Electives':
                    pass
                elif program_year == 'Year 1':
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,'No Electives',program_credits)
                    program_list.append(program_object)
                else:
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,program_elec,program_credits)
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

##
    def hard_courses(self): #Displays the top ten hardest courses for each program - Kelvin Duong Ly
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
                if sorted_cs[i][1] > sorted_cs[i+1][1]:
                    sorted_cs[i], sorted_cs[i+1] = sorted_cs[i+1], sorted_cs[i]
                    swapped = True
            if not swapped:
                break

        sorted_se = list(se_w_rankings.items())
        for mx in range(len(sorted_se)-1, -1, -1):
            swapped = False
            for i in range(mx):
                if sorted_se[i][1] > sorted_se[i+1][1]:
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
        
        
        print('Which Program\'s Top 10 Hardest Courses would you like to view?')
        print('Bachelor of Computer Science (BP094)     ||      Bachelor of Software Engineering (BP096)')
        prog_code = input('Please enter a Program\'s code: ')
        while True:
            if prog_code == 'BP094' or prog_code == 'bp094':
                print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
                print('                                               ')
                print('    Top 10 Hardest Computer Science Courses    ')
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
                print('  Top 10 Hardest Software Engineering Courses  ')
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
                ##
    
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

#loads program_by_year object 
class Program:
    def __init__(self,program_code,program_name,program_credits,program_list):
        yearly_program = LoadProgram()
        self.program_code = program_code
        self.program_name = program_name
        self.program_credits = program_credits
        self.program_list = yearly_program.load_program_objects()

    def set_program_code(self, program_code =''):
        self.program_code = program_code
    def get_code(self):
        return self.program_code

    def set_program_name(self, program_name=''):
        self.program_name = program_name
    def get_name(self):
        return self.program_name

    def set_program_credits(self, program_credits=''):
        self.program_credits = program_credits
    def get_program_credits(self):
        return self.program_credits
    
    def set_program_list(self, program_list=[]):
        self.program_list = program_list
    def get_program_list(self):
        return self.program_list

    def add_program(self,program):
        try:
            code_exist = False
            for existing_program in self.program_list:
                if program.get_code() == existing_program.get_code():
                    code_exist = True
            
            name_exist = False
            for existing_program in self.program_list:
                if program.get_name() == existing_program.get_name():
                    name_exist = True

            if code_exist == False and name_exist == False:
                self.program_list.append(program)
                print(f'Succefully added {program.get_name()}!' )
                print('')            
            elif code_exist == True or name_exist == True:
                raise ProgramAlreadyExists('This program already exists.\nPlease enter new program.')

            elif code_exist == True and name_exist == True:
                raise ProgramAlreadyExists('This program already exists.\nPlease enter new program.')
            else:
                raise ProgramAlreadyExists('This program already exists.\nPlease enter new program.')
            return self.program_list
        except ProgramAlreadyExists as error:
            print(error.mssg)
    
    def delete_program(self,program_code):
        try:
            code_exist = False
            for existing_program in self.program_list:
                if program_code.get_code().casefold() == existing_program.get_code().casefold():
                    code_exist = True
            if code_exist == True:
                self.program_list.remove(program_code)
            elif code_exist == False:
                raise ProgramDoesNotExist('This program does not exist.\nPlease enter existing program.')
            else:
                raise ProgramDoesNotExist('This program does not exist.\nPlease enter existing program.')
            return(f'Successfully removed {program_code.get_name()}')
        except ProgramDoesNotExist as error:
            print(error.mssg)


#class used to load everything from csv into this class
class LoadProgram():
    def load_program_objects(self): 
        with open('bp096_1.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)
            program_list =[]
            
            program_code = list_of_csv[1][0]
            program_name = list_of_csv[1][1]
            program_elec = list_of_csv[5][3]
            program_credits = list_of_csv[6][1]

            for x in range(1,len(list_of_csv)-2):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                if program_year == 'Elective Courses' or program_year == 'Top 5 Electives':
                    pass
                elif program_year == 'Year 1':
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,'No Electives',program_credits)
                    program_list.append(program_object)
                else:
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,program_elec,program_credits)
                    program_list.append(program_object)

        with open('bp094.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)

            program_code = list_of_csv[1][0]
            program_name = list_of_csv[1][1]
            program_elec = list_of_csv[4][3]
            program_credits = list_of_csv[5][1]

            for x in range(1,len(list_of_csv)-2):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                if program_year == 'Elective Courses' or program_year == 'Top 5 Electives':
                    pass
                elif program_year == 'Year 1':
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,'No Electives',program_credits)
                    program_list.append(program_object)
                else:
                    program_object = Program_by_year(program_code,program_name,program_year,program_core,program_elec,program_credits)
                    program_list.append(program_object)
            return program_list


#testing code
example_program1 = Program_by_year('c','c','c','c','c','c')
program_objects = example_program1.load_program_objects()
for program in program_objects:
    print(program)

example_program2 = Program_by_year('BP092','Bachelor of Beauty','Year 1','Cleaning Routine, Make-up, Hair Class','Pedicure,Manicure','124')
cs = Program('BP094','Bachelor of Computer Science','288',program_objects)
test_add = cs.add_program(example_program2)
for example in test_add:
    print(example)

test_delete = cs.delete_program(example_program1)

print(test_delete)

#everything down below was used to test methods in early stages and the methods were
#deleted and wont be needed anymore
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
print(better_list)
#print('')
#print(se_program.print_program_info('bp096_1.csv'))



testing = se_program.add_program('B096','Bacheltor of Compur Science','dsd')
#print(testing)

testing_deleting = se_program.delete_program((testing),'bp096')
print(testing_deleting)#
'''''

#testing = se_program.easy_courses()
#print(se_program.easy_courses())


    





