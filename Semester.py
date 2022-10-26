from Student import Student
from Course import Course
#from Program import Program
import csv

class CourseFullError(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class NonDuplicateError(Exception):
    def __init__(self, mssg):
        self.mssg = mssg

class CourseOffering: 
    #Add/Remove student from specific course 
    #Returns course which includes list of student objects
    def __init__(self, course_code, year, semester, max_students, student_list):
        load_data1 = Load_data()
        self.course_code = course_code
        self.year = year
        self.semester = semester
        self.max_students = max_students
        self.enrolled_students = load_data1.load_students(course_code, year, semester)
        self.student_list = student_list #Add new students into course

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

    def add_student(self, student): #Pass student object
        try:
            if len(self.enrolled_students) < self.max_students and (student not in self.enrolled_students):
                self.student_list.append(student)
            else:
                raise CourseFullError('Student cannot be added, the selected Course is full!\nPlease try another Course!')
            self.enrolled_students.extend(self.student_list)
            return self.enrolled_students
        except CourseFullError as error:
            print(error.mssg)

    def remove_student(self, student): #Remove student object that already exists
        try:
            if student in self.enrolled_students:
                self.enrolled_students.remove(student)
            else:
                raise NonDuplicateError('This student does not exist in our list of enrolled students!\nPlease remove another student!')
            return self.enrolled_students
        except NonDuplicateError as error:
            print(error.mssg)

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
    def load_allcourses(self, semester_title,year):
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            all_courses = []
            for row in list_of_csv:
                course_code = row[0]
                max_students = row[6]

                ava_sem = row[5]
                single_sems = ava_sem.split(',')
                if semester_title in single_sems:
                    course_object = CourseOffering(course_code,year,semester_title, max_students, None)
                    all_courses.append(course_object)
        return all_courses #Returns a list of courses that belong to S1 or S2

    def load_courses(self): #Courses csv file
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            course_list = []
            for info in list_of_csv:
                course_code = info[0]
                course_name = info[1]
                credit_points = int(info[4])
                prereq = info[3] #need to include course description too
                ava_sem = info[5]
                course_object = Course(course_name, course_code, credit_points, prereq, ava_sem)
                course_list.append(course_object) 
            return course_list

    def load_students(self, course_code, year, semester): #Students csv file
        with open('Students.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)

            list_of_csv = list(csv_reader)
            student_list = []
            for info in list_of_csv:
                name = info[1]
                student_id = info[0]
                dob = info[3]
                program_code = info[4]
                acad_history = info[7]
                current_enrol = info[5]
                study_plan = info[6]

                student_object = Student(name, student_id, dob, program_code, acad_history, current_enrol, study_plan)
                student_list.append(student_object)
        #Read all students objects in student_list
        #Loop through student object list and find those with matching course_code, year, semester
        
        filterstudent = []
        for student in student_list:
            student_enrol = student.get_current_enrollment().split(',')
            if year == student_enrol[0] and semester == student_enrol[1]:
                course_codes = list(student_enrol[2:])
                if course_code in course_codes:
                    year = student_enrol[0]
                    semester = student_enrol[1]
                    print(student)
                    filterstudent.append(student)
        return filterstudent

    def load_course_offerings(self, course_code, year, semester):
        max_students_value = dict()
        #with to load here
        with open('Courses.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            for info in list_of_csv:
                coursecode = info[0]
                max_students = info[6]
                max_students_value[coursecode] = max_students

        with open('Students.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            course_offering_list = []
            for row in list_of_csv:
                data_cell6 = row[5]
                info = data_cell6.split(',')
                course_codes = list(info[2:])
                if year == info[0] and semester == info[1]:
                    if course_code in course_codes:
                        year = info[0]
                        semester = info[1]
                    
                        students_list = Load_data.load_students(course_code, year, semester)
                        course_offering = CourseOffering(course_code,year,semester, max_students_value[course_code], students_list)
                        print("Julia's testing load_course_offerings")
                        print(course_offering)
                        course_offering_list.append(course_offering)
            return course_offering_list

# This file will have the Semester class
class Semester:
    def __init__(self, semester_title, year, max_students):
        load_data1 = Load_data()
        self.semester_title = semester_title
        #load all offerings this semester
        self.course_offerings = load_data1.load_allcourses(semester_title, year) #List object from Program class
        self.max_students = max_students
        #self.enrolled_students = None #List from student class (current student list)

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

    '''
    def set_EnrolledStudents(self, enrolled_students=[]):
        self.enrolled_students = enrolled_students
    def get_EnrolledStudents(self):
        return self.enrolled_students
    def print_EnrolledStudents(self):
        print('List of currently enrolled students:', self.enrolled_students)
    '''

    def __str__(self):
        string = self.get_SemesterTitle() + '\n'
        for course in self.course_offerings:
            string += course + '\n' 
        return string

#Testing class
def main():
    '''
    try:
    except:
    '''
    #Manual input of semester data
    semester1 = Semester('Semester 1 2022', 250, 'Y1')
    print(semester1)
    
    '''
    semester1 = Semester()
    name = 'Semester 2 2022 ISYS1057'
    '''

main()

