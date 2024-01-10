class Student:
    def __init__(self,enroll,name,attendence,marks,book,sem,div):
        self.enroll=enroll
        self.name=name
        self.attendence=attendence
        self.marks_percentage=marks
        self.book_issue=book
        self.sem=sem
        self.div=div
        self.printdetail()
    
    def printdetail(self):
        print(f'Name {self.name}')
        print(f'Enrollment number {self.enroll}')
        print()
    
    def Details(self):
        print("1)Check Attendence \n2)Check Marks percentage \n3)Check Book issued \n4)Check your semester details \n5)Exit")
        en=int(input("Enter your choice:"))
        if en==1:
            print(f'Attendence : {self.attendence}')
        elif en==2:
            print(f'Marks_percentage : {self.marks_percentage}')
        elif en==3:
            print(f'Book issued : {self.book_issue}')
        elif en==4:
            print(f'Semester details : {self.sem} {self.div}')
        elif en==5:
            return
        else:
            print("Wrong input")
    
    

