#Thil is testing commit
# This file will have the program class
import csv

class ProgramDoesNotExist(Exception):
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
    
    def print_program_info(self):
        print(f'Program Code: {self.p_code}\nProgram Name: {self.p_name}' )
    
    def __str__(self):
        return '\nYear: ' +self.get_year() + '\nCore Coures: ' +  self.get_pre() 
    

#answer = input('Which course plan would you like to view?')
#add and remove program for admin 

    def remove_program(self,program_name):
        try:
            if program_name in self.p_name:
                self.p_name.remove(program_name)
            else:
                raise ProgramDoesNotExist('This program does not exist.\nPlease enter existing program.')
            return self.p_name
        except ProgramDoesNotExist as error:
            print(error.mssg)
        return None

    def load_welcome_page(self):
        print('')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('')
        print('Welcome to Bachelor of Software Engineering!')
        print('')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('')

    
    def print_program_info(self,file_name):
        with open(file_name, 'r') as csv_se:
            reader = csv.reader(csv_se, delimiter=',')
            
            copy_list = [] 
            for row in reader:
                if row != '':
                    copy_list.append(row)

            info_string = ''
            if file_name == 'bp096_1.csv':
                info_string += "Program Code = " + copy_list[1][0] + '\n'
                info_string += "Program Name = " + copy_list[1][1] + '\n'
                info_string += "Total Credits = " + copy_list[6][1]
       
            elif file_name == 'bp094.csv':
                info_string += "Program Code = " + copy_list[1][0] + '\n'
                info_string += "Program Name = " + copy_list[1][1] + '\n'
                info_string += "Total Credits = " + copy_list[5][1]

        return info_string


    #loading program with arguments 

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

            for x in range(1,len(list_of_csv)-2):
                program_year = list_of_csv[x][2]
                program_core = list_of_csv[x][3]
                program_object = Program(program_code,program_name,program_year,program_core,program_elec,program_credits)
                program_list.append(program_object)
            
            return program_list
        
    def load_program_electives(self, filename):
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            list_of_csv = list(csv_reader)
        
            elective_list = []

            if filename == 'bp096_1.csv':
                elective_list.append(list_of_csv[5][3])
            
            elif filename == 'bp094.csv':
                elective_list.append(list_of_csv[4][3])
        
        return elective_list

se_program = Program('c','c','c','c','c','c')

print(se_program.print_program_info('bp094.csv'))
programs = se_program.load_program_objects('bp094.csv')
for program in programs:
    print(program)
    print('')

electives = se_program.load_program_electives('bp094.csv')
print('List of Electives:')
for elective in electives:
    print(elective + ', ')

se_program.remove_program('c')


    





