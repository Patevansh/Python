class Student:

    sampleRollNumber = 1000

    def __init__(self, name, age, grade,subject):
        Student.sampleRollNumber += 1
        self.rollNumber = Student.sampleRollNumber
        self.name = name
        self.age = age
        self.grade = grade
        self.pin = 12345
        self.subject = subject
        self.printDetails()

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollNumber}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {self.subject}")
        print(f"pin: {self.pin}")
        print()


class Teacher:
    teacherId = 0

    def __init__(self, name, subject):
        Teacher.teacherId += 1
        self.teacherId = Teacher.teacherId
        self.name = name
        self.pin = 12345
        self.subject = subject
        self.printDetails()

    def printDetails(self):
        print(f"Teacher ID: {self.teacherId}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"pin: {self.pin}")
        print()

 

class School:

    studentList = {}
    teacherList = {}

    def __init__(self):
        self.login = 0
        self.teacherLogin = 0

 

    def admitStudent(self):
        name = input("enter name of student")
        age = int(input("enter age of student"))
        grade = input("enter grade of student")
        num = int(input("enter num of subjects"))
        sub = {}
        for i in range(num):
          subname = input("enter name of subjects")

          k = f'subject{i+1}'
          sub.update({k:subname})

        student = Student(name, age, grade,sub)
        School.studentList.update({student.rollNumber: student})

    def studentApp(self):
        self.studentLogin()

    def studentLogin(self):
        roll_number = int(input('Enter your roll number: '))
        if roll_number in School.studentList:
            pin = int(input('Enter your pin number:'))
            x = School.studentList[roll_number]
            if pin == x.pin:
              print('Welcome!')
              self.login = roll_number
              self.studentMenu()
            else:
              print('please enter a valid pin')

        else:
            print('Invalid roll number.')


    def studentMenu(self):
        print('Press 1 to check your details')
        print('Press 2 to change pin')
        print('Press 3 to exit')
        choice = int(input())

        if choice == 1:
            self.checkStudentDetails()
            self.studentMenu()
        elif choice == 2:
            self.changePin()
        elif choice == 3:
            pass

    def changePin(self):
      pin = int(input("enter your current pin"))
      if pin == School.studentList[self.login].pin:
         newPin = int(input("enter your new pin"))
         School.studentList[self.login].pin = newPin
         print("your pin has been changed successfully")

    def checkStudentDetails(self):
        student = School.studentList[self.login]
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.rollNumber}")
        print(f"Age: {student.age}")
        print(f"Grade: {student.grade}")
        print(f"Subjects: {student.subject}")
        print()

    def hireTeacher(self, name, subject):
        teacher = Teacher(name, subject)
        School.teacherList.update({teacher.teacherId: teacher})

    def teacherApp(self):
        self.teacherLoginapp()

    def teacherLoginapp(self):
        teacher_id = int(input('Enter your teacher ID: '))
        if teacher_id in School.teacherList:
          p = int(input("enter your pin"))
          if p == School.teacherList[teacher_id].pin:
            print('Welcome!')
            self.teacherLogin = teacher_id
            self.teacherMenu()
          else:
            print('you have entered a wrong pin')
        else:
            print('Invalid teacher ID.')

    def teacherMenu(self):
        print('Press 1 to check your details')
        print('Press 2 to change pin')
        print('Press 3 to exit')
        choice = int(input())
        if choice == 1:
            self.checkTeacherDetails()
            self.teacherMenu()
        elif choice == 2:
            self.TeacherChangePin()

        elif choice == 3:
            pass


    def TeacherChangePin(self):
      pin = int(input("enter your current pin"))
      if pin == School.teacherList[self.teacherLogin].pin:
         newPin = int(input("enter your new pin"))
         School.teacherList[self.teacherLogin].pin = newPin
         print("your pin has been changed successfully")

    def checkTeacherDetails(self):
        teacher = School.teacherList[self.teacherLogin]
        print(f"Teacher ID: {teacher.teacherId}")
        print(f"Name: {teacher.name}")
        print(f"Subject: {teacher.subject}")
        print()

 


school = School()
school.admitStudent()
school.hireTeacher('master roshi', 'MartialArt')
school.hireTeacher('priyanshu', 'Dsa')
# Student login
school.studentApp()

school.teacherApp()