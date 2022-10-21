#Testing Commit Kelvin
# This file will have the student class
from turtle import st


class Student:
    def __init__(self, name, student_id, DOB, program_code, academic_history, current_enrollment, study_plan):
        self.name = name
        self.student_id = student_id
        self.DOB = DOB
        self.program_code = program_code
        self.academic_history = academic_history
        self.current_enrollment = current_enrollment
        self.study_plan = study_plan

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
        self.academic_history = academic_history
    def get_academic_history(self):
        return self.academic_history
    def print_academic_history(self):
        string = 'Your academic history: '
        for i in range(len(self.academic_history[0])):
            string += '\n'
            for j in self.academic_history:
                string += str(j[i]) + ' '
        print(string)

    def set_current_enrollment(self, current_enrollment = ''):
        self.current_enrollment = current_enrollment
    def get_current_enrollment(self):
        return self.current_enrollment
    def print_current_enrollment(self):
        String = 'Your Current Enrollment:'
        for i in self.current_enrollment:
            String += '\n'
            for j in i:
                String += j + ' '
        print(String)

    def set_study_plan(self, study_plan = ''):
        self.study_plan = study_plan
    def get_study_plan(self):
        return self.study_plan
    def print_study_plan(self):
        String = 'Your Study Plan:'
        for i in self.study_plan:
            String += '\n'
            for j in i:
                String += j + ' '
        print(String)

    def __str__(self):
        String = ''
        String += 'Name: ' + self.name
        String += '\nStudent ID: ' + self.student_id
        String += '\nDate of birth: ' + self.DOB
        String += '\nCurrently enrolled program: ' + self.program_code
        String += '\nAcademic History: ' 
        for i in self.academic_history.split('! '):
            String += '\n'
            i.strip()
            for j in i.split(','):
                String += j + ' '
        String += '\nCurrent enrollment: '
        for i in self.current_enrollment.split(','):
            String += ' '
            for j in i:
                String += j
        String += '\nStudy plan: '
        for i in self.study_plan.split('! '):
            String += '\n'
            for j in i.split(','):
                String += j + ' '

        return String

#Testing stuff# testing again
name = 'Kelvin'
student_id = 's3953996'
dob = '18/09/2001'
program_code = 'BP094GEN8'
academic_history = 'Y1,S1,COSC2801,89,HD ! Y1,S1,MATH2411,70,DI ! Y1,S1,COSC2803,63,CR ! Y1,S2,COSC2802,52,PA ! Y1,S2,MATH2412, 32, NN ! Y1,S2,COSC2804,55,PA ! '
current_enrollment = 'Y1,S1,COSC2801,MATH2411,COSC2803'
study_plan = 'Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235 ! Y2,S2,COSC1107,COSC1114,COSC2299,COSC2673 ! '
student1 = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
student1.set_name(name)
student1.set_student_id(student_id)
student1.set_DOB(dob)
student1.set_program_code(program_code)
student1.set_current_enrollment(current_enrollment)
student1.set_study_plan(study_plan)
student1.set_academic_history(academic_history)
print(student1)