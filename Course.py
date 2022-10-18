c_list = []
class Course:
    
    def __init__(self,course_code,title,credit_points,prerequisites,ava_sem):
        self.c_code = course_code
        self.c_title = title
        self.c_points = credit_points
        self.c_pre = prerequisites
        self.c_sem =ava_sem   
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
    life = Course(3000,"Software",24,None,"S1")
    life1 = Course(1342,"Bachelor of Engineering",200,None,"S1")
    life2 = Course(1342,"Bachelor of Engineering",200,None,"S1")
    life3 = Course(1342,"Bachelor of Engineering",200,None,"S1")
    life4 = Course(2,"Bachelor of Engineering",200,None,"S1")
    life5 = Course(1342,"Bachelor of Engineering",200,None,("S1","S2"))
    
    printinfo()
    



    
        
main()



            
        