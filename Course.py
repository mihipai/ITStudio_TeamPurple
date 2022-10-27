c_list = []

import csv
class Course:
    
    def __init__(self,course_code,title, course_description,credit_points,prerequisites,ava_sem):
        self.c_code = course_code
        self.c_title = title
        self.c_des = course_description
        self.c_points = credit_points
        self.c_pre = prerequisites
        self.c_sem =[ava_sem]
        c_list.append([course_code,title,course_description,credit_points,prerequisites,ava_sem])
    
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

    def addCourse(self,course_code,title, course_description,credit_points,prerequisites,ava_sem):
        Course(course_code,title, course_description,credit_points,prerequisites,ava_sem)

    def SearchCourse(self, C_code): ### Uses the Course Code to search for the Course
        num = len(c_list)
        stri = ""
        for x in range(num):
            
            if c_list[x][0] == C_code:
                stri += "|||||||||||||||||||||||||||||||||||||||||\n\n"            
                stri += "Course Code = " + str(c_list[x][0]) + '\n'
                stri += "\nTitle = " + str(c_list[x][1]) + '\n'
                stri += "\nCourse Description = " + str(c_list[x][2]) + '\n'
                stri += "\nCredit Points = " + str(c_list[x][3]) + '\n'
                stri += "\nPreRequirements = " + str(c_list[x][4]) + '\n'
                stri += "\nAvaivable Semster = " + str(c_list[x][5])
                stri += '\n\n'
                stri += "|||||||||||||||||||||||||||||||||||||||||\n\n\n\n"
        return print(stri)

    def removeCourse(self):
        pass        


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
                Course(course_code, course_name, course_des, credit_points, prereq, ava_sem)
                
            
    def __str__():    
        stri = ""
        for x in range(len(c_list)):
            stri += "|||||||||||||||||||||||||||||||||||||||||\n\n"            
            stri += "Course Code = " + str(c_list[x][0]) + '\n'
            stri += "\nTitle = " + str(c_list[x][1]) + '\n'
            stri += "\nCourse Description = " + str(c_list[x][2]) + '\n'
            stri += "\nCredit Points = " + str(c_list[x][3]) + '\n'
            stri += "\nPreRequirements = " + str(c_list[x][4]) + '\n'
            stri += "\nAvaivable Semster = " + str(c_list[x][5])
            stri += '\n\n'
            stri += "|||||||||||||||||||||||||||||||||||||||||\n\n\n\n"
        return stri


def main():
    Course.load_courses(self="self",filename='Courses.csv')
    Course.SearchCourse("self", "COSC2801")



    
        
main()



            
        