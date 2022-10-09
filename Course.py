class Course:

    def __init__(self):
        self.c_list = []

    def addCourse(self,course_code,title,credit_points,prerequisites,ava_sem):
        self.c_code = course_code
        self.c_title = title
        self.c_points = credit_points
        self.c_pre = prerequisites
        self.c_sem =ava_sem
        self.c_list.append([course_code,title,credit_points,prerequisites,ava_sem])
    
    
    def getCourseCode(self):
        return self.c_code
    
    def getTitle(self):
        return self.c_title
    
    def getCreditPoints(self):
        return self.c_points
    
    def getPreRequirement(self):
        return self.c_pre
    
    def getAvaivableSemester(self):
        return self.c_sem
    
    def __str__(self):
        stri = ""
        for x in range(len(self.c_list)):
            
            stri += "Course Code = " + str(self.c_list[x][0])
            stri += "\nTitle = " + str(self.c_list[x][1])
            stri += "\nCredit Points = " + str(self.c_list[x][2])
            stri += "\nPreRequirements = " + str(self.c_list[x][3])
            stri += "\nAvaivable Semster = " + str(self.c_list[x][4])
            stri += '\n\n'
            print(x)
        return stri

def main():
    life = Course()
    life.addCourse(1342,"Bachelor of Engineering",200,None,"S1")
    life.addCourse(1342,"Bachelor of Engineering",200,None,"S1")
    life.addCourse(1342,"Bachelor of Engineering",200,None,"S1")
    life.addCourse(2,"Bachelor of Engineering",200,None,"S1")
    life.addCourse(1342,"Bachelor of Engineering",200,None,("S1","S2"))




    print(life)
        
main()



            
        