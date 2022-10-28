#Student Name: Julia Ngoc Diem Tran Phan
#Student ID: s3948825
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
    def __init__(self, course_code, course_name, year, semester, max_students):
        load_data1 = Load_data()
        self.course_code = course_code
        self.course_name = course_name
        self.year = year
        self.semester = semester
        self.max_students = int(max_students)
        self.enrolled_students = load_data1.load_students(course_code, year, semester)

    def set_CourseCode(self, course_code=''):
        self.course_code = course_code

    def get_CourseCode(self):
        return self.course_code

    def set_CourseName(self, course_name=''):
        self.course_name = course_name

    def get_CourseName(self):
        return self.course_name
    
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
            student_exist = False
            for enrol in self.enrolled_students:
                if student.get_student_id() == enrol.get_student_id():
                    student_exist = True

            if student_exist == False and len(self.enrolled_students) < self.max_students:
                self.enrolled_students.append(student)
                print(f'Student \'{student.get_name()}\' has been successfully added!\n')
            elif student_exist == True and len(self.enrolled_students) < self.max_students:
                print(f'WARNING! \'{student.get_name()}\' cannot be enrolled, they already exists in our list of enrolled students\n')
            elif student_exist == False and len(self.enrolled_students) == self.max_students:
                print(f'WARNING! \'{student.get_name()}\' cannot be enrolled, the selected Course is full!\nPlease try another Course!\n')
            else: #Student exists and course is full
                raise CourseFullError(f'WARNING! \'{student.get_name()}\' cannot be enrolled, they already exists in our list of enrolled students and the selected Course is full!\nPlease try another Course!\n')
            return self.enrolled_students
        except CourseFullError as error:
            print(error.mssg)

    def remove_student(self, student_id): #Remove student object based on student ID
        try:
            name_str = ''
            student_exist = False
            for enrol in self.enrolled_students:
                if student_id == enrol.get_student_id():
                    student_exist = True
                    name_str += enrol.get_name()
                    break

            if student_exist == True:
                self.enrolled_students.remove(enrol)                
                print(f'Student \'{name_str}\' has been successfully removed!\n')
            else:      
                raise NonDuplicateError(f'WARNING! \'{student_id}\' does not exist in our list of enrolled students!\nPlease remove another student!\n')
            return self.enrolled_students
        except NonDuplicateError as error:
            print(error.mssg)

    #This method formats the Course offer which includes a list of student after students are added or removed
    def __str__(self):
        formatted_str = ''
        formatted_str += 'Course Code: ' + self.get_CourseCode()
        formatted_str += '\nCourse Name: ' + self.get_CourseName()
        formatted_str += '\nYear: ' + self.get_Year()
        formatted_str += '\nSemester Title: ' + self.get_Semester()
        formatted_str += '\nMaximum Number of Students: ' +  self.get_MaxStudents() + '\n'
        formatted_str += '==============================='
        formatted_str += '\nList of Enrolled Students:\n'
        formatted_str += '===============================\n'
        if len(self.get_EnrolledStudents()) == 0:
            formatted_str += 'ERROR! The selected course has no students!'
        else:
            for enrol in self.get_EnrolledStudents():
                formatted_str += enrol.__str__() + '\n--------------------------------------\n'
        return formatted_str

    #Formats the Courses which will be displayed 
    def without_students(self):
        formatted_str = ''
        formatted_str += '========================================\n'
        formatted_str += 'Course Code: ' + self.get_CourseCode()
        formatted_str += '\nCourse Name: ' + self.get_CourseName()
        formatted_str += '\nYear: ' + self.get_Year()
        formatted_str += '\nSemester Title: ' + self.get_Semester()
        formatted_str += '\nMaximum Number of Students: ' +  self.get_MaxStudents()
        formatted_str += '\n========================================'
        return formatted_str


class Load_data:
    #Returns a list of courses that belong to Semester and Year
    def load_allcourses(self, semester_title,year):
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            all_courses = []
            for row in list_of_csv:
                course_code = row[0]
                course_name = row[1]
                max_students = row[6]

                ava_sem = row[5]
                single_sems = ava_sem.split(',')
                if semester_title in single_sems:
                    course_object = CourseOffering(course_code,course_name,year,semester_title, max_students)
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
        #Load all offerings this semester
        self.course_offerings = load_data1.load_allcourses(semester_title, year) #List object from Program class
        self.max_students = max_students
        #self.enrolled_students = None #List from student class (current student list)

    def set_SemesterTitle(self, semester_title=''):
        self.semester_title = semester_title
    def get_SemesterTitle(self):
        return str(self.semester_title)
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

    def easy_courses(self): #Julia Ngoc Diem Tran Phan - Top 10 Easy Courses
        courses_w_rankings = dict()
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            for info in list_of_csv:
                code = info[0]
                rank = int(info[8])
                courses_w_rankings[code] = rank
        
        rank_list = list(courses_w_rankings.items())
        for mx in range(len(rank_list)-1, -1, -1):
            swapped = False
            for i in range(mx):
                if rank_list[i][1] < rank_list[i+1][1]:
                    rank_list[i], rank_list[i+1] = rank_list[i+1], rank_list[i]
                    swapped = True
            if not swapped:
                break

        last_ten_courses = rank_list[:10]
        new_list = [new[0] for new in last_ten_courses]
        del last_ten_courses

        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('                                               ')
        print('            Top 10 Easiest Courses             ')
        print('                                               ')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
        #['COSC1226', 'ISYS1126', 'COSC1147', 'COSC2802', 'ISYS2405', 
        # 'MATH2412', 'INTE2376', 'COSC2799', 'COSC1183', 'COSC2471'] 
        
        with open('Courses.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            course_list = []
            for info in list_of_csv:
                course_code = info[0]
                course_name = info[1]
                descr = info[2]
                credit_points = int(info[4])
                prereq = info[3] #need to include course description too
                ava_sem = info[5]
                for new in new_list:
                    if new == course_code:
                        course_object = Course(course_name, course_code, descr, credit_points, prereq, ava_sem)
                        course_list.append(course_object) 
        return course_list[0].__str__()

    def __str__(self):
        string = 'Semester: ' + self.get_SemesterTitle() + '\n'
        if len(self.course_offerings) == 0:
            string += 'ERROR! There are no available course offerings in this Semester!'
        else:
            for course in self.course_offerings:
                string += course.without_students() + '\n\n' 
        return string

#Testing classes
def main():
    #Manual input of semester data
    '''
    #This section prints top 10 easy courses, druv might need to add self parameter in dunder string method
    ###############################################################################
    semester1 = Semester('S1','Y1',250)
    semester1.easy_courses()
    ###############################################################################
    '''
    
    '''    
    #This section adds or removes a student object from course and displays the Course-offering/Course with list of students
    ###############################################################################
    courseoffer1 = CourseOffering('COSC2801', 'Programming Bootcamp 1','Y1','S1', 4)
    #Student object named Kelvin
    name = 'Kelvin'
    student_id = 's3453976'
    dob = '18/09/2001'
    program_code = 'BP094GEN8'
    academic_history = 'Y1,S1,COSC2801,89,HD ! Y1,S1,MATH2411,70,DI ! Y1,S1,COSC2803,63,CR ! Y1,S2,COSC2802,52,PA ! Y1,S2,MATH2412, 32, NN ! Y1,S2,COSC2804,55,PA ! '
    current_enrollment = 'Y1,S1,COSC2801,MATH2411,COSC2803'
    study_plan = 'Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235 ! Y2,S2,COSC1107,COSC1114,COSC2299,COSC2673 ! '
    student1 = Student(name, student_id, dob, program_code, academic_history, current_enrollment, study_plan)
    name2 = 'Charlotte Jones'
    student_id2 = 's3553976'
    dob2 = '18/09/2001'
    program_code2 = 'BP096'
    academic_history2 = 'Y1,S1,COSC2801,89,HD ! Y1,S1,MATH2411,70,DI ! Y1,S1,COSC2803,63,CR ! Y1,S2,COSC2802,52,PA ! Y1,S2,MATH2412, 32, NN ! Y1,S2,COSC2804,55,PA ! '
    current_enrollment2 = 'Y1,S1,COSC2801,MATH2411,COSC2803'
    study_plan2 = 'Y1,S2,COSC2802,MATH2412,COSC2804 ! Y2,S1,COSC2123,COSC1076,ISYS1118,COSC1235 ! Y2,S2,COSC1107,COSC1114,COSC2299,COSC2673 ! '
    student2 = Student(name2, student_id2, dob2, program_code2, academic_history2, current_enrollment2, study_plan2)
    student_id3 = 's386894' #Arun Weaver
    #Add or Remove student object from specific course
    courseoffer1.add_student(student1)
    courseoffer1.add_student(student2)
    courseoffer1.remove_student(student_id3)
    print(courseoffer1)
    ###############################################################################
    '''

    '''
    #This section prints the list of Courses/Course-offerings for a specific Semester and Year
    ###############################################################################
    semester1 = Semester('S1','Y1', 250)
    print(semester1)
    ###############################################################################
    '''

main()

