from Student import Student
from Course import Course
from Program import Program
import csv

class CourseOffering: #Calculation in adding/removing a student from a specific course offer
    def __init__(self,course_code,year,semester, max_students, student_list):
        load_data1 = Load_data()
        self.courseinfo = Load_data.load_courses() 
        #could add course information inside CourseOffering class string
        self.course_code = course_code
        self.year = year
        self.semester = semester
        self.max_students = max_students
        self.enrolled_students = load_data1.load_students()
        self.student_list = student_list #add new students in course

    def set_CourseCode(self, course_code=''):
        self.course_code = course_code

    def get_CourseCode(self):
        return self.course_code
    
    def set_Year(self, year=''):
        self.year = year

    def get_Year(self):
        return self.year

    def set_Semester(self, semester=''):
        self.semester = semester

    def get_Semester(self):
        return self.semester
    
    def set_MaxStudents(self, max_students=0):
        self.max_students = max_students

    def get_MaxStudents(self):
        return self.max_students

    def set_EnrolledStudents(self, enrolled_students=[]):
        self.enrolled_students = enrolled_students

    def get_EnrolledStudents(self):
        return self.set_EnrolledStudents

    def add_student(self, student): #pass class objects
        if len(self.enrolled_students) < self.max_students and (student not in self.enrolled_students):
            self.student_list.append(student)
        else:
            self.student_list
            #Student cannot be added, no places left for course enrollment
        self.enrolled_students.extend(self.student_list)
        return self.enrolled_students

    def remove_student(self, student):            
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        else:
            return self.enrolled_students
        return self.enrolled_students

    def __str__(self):
        formatted_str = ''
        formatted_str += 'Course Code: ' + self.get_CourseCode()
        formatted_str += '\nYear: ' + self.get_Year()
        formatted_str += '\nSemester Title: ' + self.get_Semester()
        formatted_str += '\nMaximum Number of Students: ' +  self.get_MaxStudents()
        formatted_str += '\nList of Enrolled Students:\n'
        for enrol in self.get_EnrolledStudents():
            formatted_str += enrol
        return formatted_str


class Load_data:
    def load_courses(filename): #Courses csv file
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            courselist = [] # list of course objects
            first_row = True
            for row in csv_reader:
                if first_row:
                    first_row = False
                    continue
                course_code = row[0]
                course_name = row[1]
                credit_points = int(row[4])
                prereq = row[3] #need to include course description too
                ava_sem = row[5]
                course_object = Course(course_name, course_code, credit_points, prereq, ava_sem)
                courselist.append(course_object) 
            return courselist

    def load_students(filename, course_codes, year, semester): #Students csv file
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            studentlist = [] # list of course objects
            filterstudent = []
            first_row = True
            for row in csv_reader:
                if first_row:
                    first_row = False
                    continue
                name = row[1]
                student_id = row[0]
                dob = row[3]
                program_code = row[4]
                academic_history = row[7]
                current_enrollment = row[5]
                study_plan = row[6]
                student_object = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
                studentlist.append(student_object)
            #read all students objects
            #loop through student object list and find those with match course_code, year, semester
            
            formatted_str = ''
            first_row = True
            for row in csv_reader:
                if first_row:
                    first_row = False
                    continue
                data_cell6 = row[5]
                small_row = data_cell6.split(',')
                year == small_row[0]
                semester == small_row[1]
                course_codes = list(small_row[2:])
                formatted_str += year + ','
                formatted_str += semester + ','
                for course in course_codes:
                    if not course == course_codes[-1]:
                        formatted_str += course + ','
                    else:
                        formatted_str += course
                for student in studentlist:
                    if formatted_str == student.get_current_enrollment(): 
                    #trying to call current enrollment inside student object from Student class
                        filterstudent.append(student)
            return filterstudent

    def load_course_offerings(filename, filename2, course_code, year, semester): #Courses & Students csv files
        max_students_value = dict()
        #with to load here
        with open(filename2, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            first_row = True
            for row in csv_reader:
                if first_row:
                    first_row = False
                    continue
                coursecode = row[0]
                maxno = row[6]
                max_students_value[coursecode] = maxno

        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            course_offerings = [] # list of course objects
            first_row = True
            for row in csv_reader:
                if first_row:
                    first_row = False
                    continue
                data_cell6 = row[5]
                small_row = data_cell6.split(',')
                course_codes = list(row[2:])
                if year == small_row[0] and semester == small_row[1]:
                    if course_code in course_codes:
                        year = small_row[0]
                        semester = small_row[1]
                    
                        students_list = Load_data.load_students(filename,course_code, year, semester)
                        course_offering = CourseOffering(course_code,year,semester, max_students_value[course_code], students_list)
                        course_offerings.append(course_offering)
            return course_offerings

# This file will have the Semester class
class Semester:
    def __init__(self, semester_title, max_students,year):
        load_data1 = Load_data()
        self.semester_title = semester_title
        #load all offerings this semester
        self.course_offerings = load_data1.load_course_offerings(semester_title, year) #List object from Program class
        self.max_students = max_students
        self.enrolled_students = load_data1.load_students() #List from student class (current student list)

    def set_SemesterTitle(self, semester_title=''):
        self.semester_title = semester_title
    def get_SemesterTitle(self):
        return self.semester_title
    def print_SemesterTitle(self):
        print('Current Semester:', self.semester_title)

    def set_CourseOfferings(self, course_offerings=[]):
        self.course_offerings = course_offerings
    def get_CourseOfferings(self):
        return self.course_offerings
    def print_CourseOfferings(self):
        print('List of available Course Offerings:', self.course_offerings)

    def set_MaxStudents(self, max_students=0):
        self.max_students = max_students
    def get_MaxStudents(self):
        return self.max_students
    def print_MaxStudents(self):
        print('Maximum number of students:', self.max_students)

    def set_EnrolledStudents(self, enrolled_students=[]):
        self.enrolled_students = enrolled_students
    def get_EnrolledStudents(self):
        return self.enrolled_students
    def print_EnrolledStudents(self):
        print('List of currently enrolled students:', self.enrolled_students)

    def __str__(self):
        string = self.get_SemesterTitle() + '\n'
        for course in self.course_offerings:
            string += course + '\n' 
        return string

#Testing class
'''
semester1 = Semester()
name = 'Semester 2 2022 ISYS1057'
course_list = ['Programming Techniques', 'User-centred Design', 'Further Programming', 
                'Database Concepts', 'Introduction to Analytics']
courses = []
courses.append(course_list)
courses.append(course_code)
courses.append(credit_points)

semester1.set_CourseOfferings(courses)
semester1.print_CourseOfferings()
semester1.set_SemesterTitle(name)
semester1.print_SemesterTitle()

students = []
student_name = ['Reginald Sweeney', 'Kayley Nairn', 'Nur Clements', 'Nataniel Koch', 'Camilla Feeney']
students.append(student_name)
students.append(student_id)
students.append(dob)
'''

