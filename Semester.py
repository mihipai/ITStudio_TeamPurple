#Author: Julia Ngoc Diem Tran Phan - s3948825
from Student import Student
#from Course import Course
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
        self.max_students = int(max_students)
        self.enrolled_students = load_data1.load_students(course_code, year, semester)
        self.student_list = student_list

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
        return str(self.max_students)

    def set_EnrolledStudents(self, enrolled_students=[]):
        self.enrolled_students = enrolled_students

    def get_EnrolledStudents(self):
        return self.enrolled_students

    def add_student(self, student): #Add new student object into course
        try:
            for enrol in self.enrolled_students:
                if student.get_student_id() == enrol.get_student_id():
                    print('Student cannot be enrolled, they already exists in our list of enrolled students!\n')
                else:
                    self.student_list.append(student)
            if len(self.enrolled_students) < self.max_students:
                self.student_list.append(student)
            else:
                raise CourseFullError('Student cannot be enrolled, the selected Course is full!\nPlease try another Course!\n')
            self.enrolled_students.extend(self.student_list)
            return self.enrolled_students
        except CourseFullError as error:
            print(error.mssg)

    def remove_student(self, student): #Remove student object that already exists in course
        try:
            for enrol in self.enrolled_students:
                if student.get_student_id() == enrol.get_student_id():
                    self.enrolled_students.remove(student)
                else:
                    raise NonDuplicateError('This student does not exist in our list of enrolled students!\nPlease remove another student!\n')
            return self.enrolled_students
        except NonDuplicateError as error:
            print(error.mssg)

    #This method formats the Course offer which includes a list of student after students are added or removed
    def __str__(self):
        formatted_str = ''
        formatted_str += 'Course Code: ' + self.get_CourseCode()
        formatted_str += '\nYear: ' + self.get_Year()
        formatted_str += '\nSemester Title: ' + self.get_Semester()
        formatted_str += '\nMaximum Number of Students: ' +  self.get_MaxStudents() + '\n'
        formatted_str += '==============================='
        formatted_str += '\nList of Enrolled Students:\n'
        formatted_str += '===============================\n'
        if len(self.get_EnrolledStudents()) == 0:
            formatted_str += 'There are no students in this course!'
        else:
            for enrol in self.get_EnrolledStudents():
                formatted_str += enrol.__str__() + '\n'
        return formatted_str

    #Formats the Courses which will be displayed 
    def without_students(self):
        formatted_str = ''
        formatted_str += '================================\n'
        formatted_str += 'Course Code: ' + self.get_CourseCode()
        formatted_str += '\nYear: ' + self.get_Year()
        formatted_str += '\nSemester Title: ' + self.get_Semester()
        formatted_str += '\nMaximum Number of Students: ' +  self.get_MaxStudents()
        formatted_str += '\n================================'
        return formatted_str


class Load_data:
    #Returns a list of courses that belong to Semester or Year
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
        return all_courses

    #Similarly this method was used to load a list of Courses but is now not used
    '''
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
    '''

    def load_students(self, course_code, year, semester):
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
                    filterstudent.append(student)
        return filterstudent

    #This method was made to return a list of course offerings but is now never used
    '''
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
        '''

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
        string = 'Semester: ' + self.get_SemesterTitle() + '\n'
        if len(self.course_offerings) == 0:
            string += 'There are no available course offerings in this Semester'
        else:
            for course in self.course_offerings:
                string += course.without_students() + '\n\n' 
        return string

#Testing class
def main():
    print('=====================================================')
    print('                Available Semesters                  ')
    print('=====================================================')
    print('To select Semester 1, type S1')
    print('To select Semester 2, type S2')

    print('=====================================================')
    print('                 Available Years                     ')
    print('=====================================================')
    print('To select Year 1, type Y1')
    print('To select Year 2, type Y2')
    print('To select Year 3, type Y3')
    print('To select Year 4, type Y4\n')


    '''
    #Manual input of semester data
    #This section adds or removes a student object from course and displays the Course-offering/Course with list
    ###############################################################################
    courseoffer1 = CourseOffering('COSC2801','Y1','S1', '250', None)
    #Student object named Kelvin
    name = 'Kelvin'
    student_id = 's3953996'
    dob = '18/09/2001'
    program_code = 'BP094GEN8'
    academic_history = 'Y1,S1,COSC2801,89,HD ! Y1,S1,MATH2411,70,DI ! Y1,S1,COSC2803,63,CR ! Y1,S2,COSC2802,52,PA ! Y1,S2,MATH2412, 32, NN ! Y1,S2,COSC2804,55,PA ! '
    current_enrollment = 'Y1,S1,COSC2801,MATH2411,COSC2803'
    study_plan = 'Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235 ! Y2,S2,COSC1107,COSC1114,COSC2299,COSC2673 ! '
    student1 = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
    #Add or Remove student object from specific course
    courseoffer1.add_student(student1)
    courseoffer1.remove_student(student1)
    print(courseoffer1)
    ###############################################################################

    #This section prints the list of Courses/Course-offerings for a specific Semester and Year
    ###############################################################################
    semester1 = Semester('S2','Y1', 250)
    print(semester1)
    ###############################################################################
    '''


main()

