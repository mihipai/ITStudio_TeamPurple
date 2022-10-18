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

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def print_name(self):
        print(self.name)

    def set_student_id(self, student_id):
        self.student_id = student_id
    def get_student_id(self):
        return self.student_id
    def print_student_id(self):
        print(self.student_id)

    def set_DOB(self, DOB):
        self.DOB = DOB
    def get_DOB(self):
        return self.DOB
    def print_DOB(self):
        print(self.DOB)
    
    def set_program_code(self, program_code):
        self.program_code = program_code
    def get_program_code(self):
        return self.program_code
    def print_program_code(self):
        print(self.program_code)
    
    def set_academic_history(self, academic_history):
        self.academic_history = academic_history
    def get_academic_history(self):
        return self.academic_history
    def print_academic_history(self):
        print(self.academic_history)

    def set_current_enrollment(self, current_enrollment):
        self.current_enrollment = current_enrollment
    def get_current_enrollment(self):
        return self.current_enrollment
    def print_current_enrollment(self):
        print(self.current_enrollment)

    def set_study_plan(self, study_plan):
        self.study_plan = study_plan
    def get_study_plan(self):
        return self.study_plan
    def print_study_plan(self):
        print(self.study_plan)

    