class Address:
    def __init__(self, street, city, state, postalCode, country):
        self._street = street
        self._state = state
        self._city = city
        self._postalCode = postalCode
        self._country = country

    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_postalCode(self):
        return self._postalCode

    def get_country(self):
        return self._country

    def set_street(self, street):
        self._street = street

    def set_city(self, city):
        self._city = city

    def set_state(self, state):
        self._state = state

    def set_postalCode(self, postalCode):
        self._postalCode = postalCode

    def set_country(self, country):
        self._country = country


class Person:
    def __init__(self, name, phoneNumber, emailAddress):
        self._name = name
        self._phoneNumber = phoneNumber
        self._emailAddress = emailAddress
        self._address = None
    
    def purchaseParkingPass(self):
        pass

    def get_name(self):
        return self._name

    def get_phoneNumber(self):
        return self._phoneNumber

    def get_emailAddress(self):
        return self._emailAddress

    def get_address(self):
        return self._address

    def set_name(self, name):
        self._name = name

    def set_phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def set_emailAddress(self, emailAddress):
        self._emailAddress = emailAddress

    def set_address(self, address):
        self._address = address


class Student(Person):
    def __init__(self, name, phoneNumber, emailAddress, studentNumber, averageMarks):
        self.set_name(name)
        self.set_phoneNumber(phoneNumber)
        self.set_emailAddress(emailAddress)
        self._studentNumber = studentNumber
        self._averageMarks = averageMarks

    def get_attributes(self):
        return {
            "name": self.get_name(),
            "phoneNumber": self.get_phoneNumber(),
            "emailAddress": self.get_emailAddress(),
            "studentNumber": self.get_studentNumber(),
            "averageMarks": self.get_averageMarks()
        }
    
    def isEligibleToEnroll(self):
        pass

    def getSeminarsTaken(self):
        pass

    def get_studentNumber(self):
        return self._studentNumber

    def get_averageMarks(self):
        return self._averageMarks

    def set_studentNumber(self, studentNumber):
        self._studentNumber = studentNumber

    def set_averageMarks(self, averageMarks):
        self._averageMarks = averageMarks


class Professor(Person):
    def __init__(self, name, phoneNumber, emailAddress, salary, staffNumber, yearOfservices, numberOfClasses):
        self.set_name(name)
        self.set_phoneNumber(phoneNumber)
        self.set_emailAddress(emailAddress)
        self._salary = salary
        self._staffNumber = staffNumber
        self._yearOfservices = yearOfservices
        self._numberOfClasses = numberOfClasses
        self.supervised_students=[]
    
    def supervise(self,student):
        if len(self.supervised_students)<5:
            self.supervised_students.append(student)
        else:
            print("Professor can supervise up to 5 students only.")

    def get_attributes(self):
        return {
            "name": self.get_name(),
            "phoneNumber": self.get_phoneNumber(),
            "emailAddress": self.get_emailAddress(),
            "salary": self.get_salary(),
            "staffNumber": self.get_staffNumber(),
            "yearOfservices": self.get_yearOfservices(),
            "numberOfClasses": self.get_numberOfClasses()
        }
        
    def get_salary(self):
        return self._salary

    def get_staffNumber(self):
        return self._staffNumber

    def get_yearOfservices(self):
        return self._yearOfservices

    def get_numberOfClasses(self):
        return self._numberOfClasses

    def set_salary(self, salary):
        self._salary = salary

    def set_staffNumber(self, staffNumber):
        self._staffNumber = staffNumber

    def set_yearOfservices(self, yearOfservices):
        self._yearOfservices = yearOfservices

    def set_numberOfClasses(self, numberOfClasses):
        self._numberOfClasses = numberOfClasses

