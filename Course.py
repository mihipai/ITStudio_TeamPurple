c_list = []

import csv
class Course:
    
    def __init__(self,course_code,title,credit_points,prerequisites,ava_sem):
        self.c_code = course_code
        self.c_title = title
        self.c_points = credit_points
        self.c_pre = prerequisites
        self.c_sem =[ava_sem]
        c_list.append([course_code,title,credit_points,prerequisites,ava_sem])
    
    
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

    def load_courses(self, filename): #Courses csv file
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headings = next(csv_reader)
            list_of_csv = list(csv_reader)
            
            for info in list_of_csv:
                course_code = info[0]
                course_name = info[1]
                credit_points = info[4]
                prereq = info[3] #need to include course description too
                ava_sem = info[5]
                Course(course_name, course_code, credit_points, prereq, ava_sem)
                
            return c_list

    
def printinfo():    
    stri = ""
    for x in range(len(c_list)):            
        stri += "Course Code = " + str(c_list[x][0])
        stri += "\nTitle = " + str(c_list[x][1])
        stri += "\nCredit Points = " + str(c_list[x][2]) 
        stri += "\nPreRequirements = " + str(c_list[x][3])
        stri += "\nAvaivable Semster = " + str(c_list[x][4])
        stri += '\n\n'
            
    print(stri)


def main():
    csv = Course.load_courses(self="self",filename='Course data.csv')
    printinfo()
    



    
        
main()



            
        