c_list = []
class CourseDoesNotExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg
class CourseDoesExist(Exception):
    def __init__(self, mssg):
        self.mssg = mssg
import csv
class Course:
    
    def __init__(self,course_code,title, course_description,credit_points,prerequisites,ava_sem, g_dis):
        self.c_code = course_code
        self.c_title = title
        self.c_des = course_description
        self.c_points = credit_points
        self.c_pre = prerequisites
        self.c_sem =[ava_sem]
        self.c_dis = [g_dis]
        c_list.append([course_code,title,course_description,credit_points,prerequisites,ava_sem, g_dis.split(",")])
    
    def getCourseDescription(self):
        return str(self.c_des)

    def getCourseCode(self):
        return str(self.c_code)
    
    def getTitle(self):
        return self.c_title
    
    def getCreditPoints(self):
        return self.c_points
    
    def getPreRequirement(self):
        return self.c_pre
    
    def getAvaivableSemester(self):
        return self.c_sem

    def addCourse(self,course_code,title, course_description,credit_points,prerequisites,ava_sem,g_dis): ### Uses the Course Code to search for the Course
        num = len(c_list)
        try:
            for x in range(num):
                
                if c_list[x][0] == course_code:
                    raise CourseDoesExist("The Course you want to add, already exist!!")
                elif x == (num-1):
                    Course(course_code,title, course_description,credit_points,prerequisites,ava_sem, g_dis)
                    return print("Course added!")
        except CourseDoesExist as error:
            print(error.mssg)


        

    def removeCourse(self,C_code): ### Uses the Course Code to search for the Course
        num = len(c_list)
        
        try:
            for x in range(num):
                
                if c_list[x][0] == C_code:
                    print("Course " + c_list[x][1] + " has been removed")
                    c_list.pop(x)
                    
                elif x == (num-1):
                    raise CourseDoesNotExist("The Course you want to remove does not exist!!")
            
        except CourseDoesNotExist as error:
            print(error.mssg)

        

    def SearchCourse(self, C_code): ### Uses the Course Code to search for the Course
        
        num = len(c_list)
        count = 0
        stri = ""
        try:
            for x in range(num):
                if c_list[x][0] == C_code:
                    stri += "|||||||||||||||||||||||||||||||||||||||||\n\n"            
                    stri += "Course Code = " + str(c_list[x][0]) + '\n'
                    stri += "\nTitle = " + str(c_list[x][1]) + '\n'
                    stri += "\nCourse Description = " + str(c_list[x][2]) + '\n'
                    stri += "\nCredit Points = " + str(c_list[x][3]) + '\n'
                    stri += "\nPreRequirements = " + str(c_list[x][4]) + '\n'
                    stri += "\nAvaivable Semster = " + str(c_list[x][5]) + '\n'
                    stri += "\nGrade Distribution = " + str(c_list[x][6]) 
                    stri += '\n\n'
                    stri += "|||||||||||||||||||||||||||||||||||||||||\n\n\n\n"
                    count += 1
            if count == 0:
                raise CourseDoesNotExist("The Course you searched for does not exist!!")
            return print(stri)
        except CourseDoesNotExist as error:
            print(error.mssg)


    def SearchCourseDistribution(self, C_code): ### Uses the Course Code to search for the Course
        Course.load_courses(self,"Courses.csv")
        num = len(c_list)
        count = 0
        stri = ""
        try:
            for x in range(num):                
                if c_list[x][0] == C_code:
                    stri += "|||||||||||||||||||||||||||||||||||||||||\n\n"            
                    stri += "Course Code = " + str(c_list[x][0]) + '\n'
                    stri += "\nTitle = " + str(c_list[x][1]) + '\n'
                    stri += "\nGrade Distribution = " + str(c_list[x][6])
                    stri += '\n\n'
                    stri += "|||||||||||||||||||||||||||||||||||||||||\n\n\n\n"
            if count == 0:
                raise CourseDoesNotExist("The Course you searched for does not exist!!")
            return print(stri)
        except CourseDoesNotExist as error:
            print(error.mssg)

    
    
 


    def load_courses(self, filename): #
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            
            for x in range(len(list_of_csv)):
                course_code = list_of_csv[x][0]
                course_name = list_of_csv[x][1]
                course_des = list_of_csv[x][2]
                credit_points = list_of_csv[x][4]
                prereq = list_of_csv[x][3] 
                ava_sem = list_of_csv[x][5]
                g_dis = list_of_csv[x][9]
                Course(course_code, course_name, course_des, credit_points, prereq, ava_sem, g_dis)
            
                
            
    def __str__(self):    
        stri = ""
        for x in range(len(c_list)):
            stri += "|||||||||||||||||||||||||||||||||||||||||\n\n"            
            stri += "Course Code = " + str(c_list[x][0]) + '\n'
            stri += "\nTitle = " + str(c_list[x][1]) + '\n'
            stri += "\nCourse Description = " + str(c_list[x][2]) + '\n'
            stri += "\nCredit Points = " + str(c_list[x][3]) + '\n'
            stri += "\nPreRequirements = " + str(c_list[x][4]) + '\n'
            stri += "\nAvaivable Semster = " + str(c_list[x][5]) + '\n'
            stri += "\nGrade Distribution = " + str(c_list[x][6]) 
            stri += '\n\n'
            stri += "|||||||||||||||||||||||||||||||||||||||||\n\n\n\n"
        print(stri)


