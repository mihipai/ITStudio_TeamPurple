#Testing Commit Kelvin
# This file will have the student class
from turtle import st


class Student:
    def _init_(self, name, student_id, DOB, program_code, academic_history, current_enrollment, study_plan):
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
    
    def set_academic_history(self, academic_history = []):
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

    def set_current_enrollment(self, current_enrollment = []):
        self.current_enrollment = current_enrollment
    def get_current_enrollment(self):
        return self.current_enrollment
    def print_current_enrollment(self):
        print(f'Your current enrollment: {self.current_enrollment}')

    def set_study_plan(self, study_plan = []):
        self.study_plan = study_plan
    def get_study_plan(self):
        return self.study_plan
    def print_study_plan(self):
        print(f'Your current study plan: {self.study_plan}')

    def print_all(self):
        String = ''
        String += 'Name: ' + self.name
        String += '\nStudent ID: ' + self.student_id
        String += '\nDate of birth: ' + self.DOB
        String += '\nCurrently enrolled program: ' + self.program_code
        String += '\nAcademic History: ' 
        for i in range(len(self.academic_history[0])):
            String += '\n'
            for j in self.academic_history:
                String += str(j[i]) + ' '
        String += '\nCurrent enrollment: '
        for i in self.current_enrollment:
            String += '\n'
            for j in i:
                String += j + ' '
        String += '\nStudy plan: '
        for i in self.study_plan:
            String += '\n'
            for j in i:
                String += j + ' '

        print(String)

#Testing stuff# testing again
student1 = Student()
name = 'Kelvin'
student_id = 's3953996'
dob = '18/09/2001'
program_code = 'BP094GEN8'
Subject_list = ['English', 'Math', 'Chemistry', 'Biology', 'Psychology']
Mark = [80, 82, 75, 90, 88]
Grade = ['A', 'A', 'B+', 'A+', 'A']
academic_history = []
academic_history.append(Subject_list)
academic_history.append(Mark)
academic_history.append(Grade)
current_enrollment = [['Y2', 'S2', 'COSC2800', 'IT Studio 2'], ['Y2', 'S2', 'MATH2412', 'Mathematics for Computing 2']]
study_plan = [['Y2', 'S2', 'COSC2800', 'IT Studio 2'],['Y3', 'S1', 'COSC2800', 'IT Studio 2']]
student1.set_name(name)
student1.set_student_id(student_id)
student1.print_name()
student1.set_DOB(dob)
student1.set_program_code(program_code)
student1.set_current_enrollment(current_enrollment)
student1.set_study_plan(study_plan)
student1.set_academic_history(academic_history)
student1.print_all()