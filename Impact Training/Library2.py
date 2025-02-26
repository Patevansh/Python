class Librarian:
    def __init__(self, id, name, contact_no, password):
        self._id = id
        self._name = name
        self._contact_no = contact_no
        self._password = password

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact_no(self):
        return self._contact_no

    def set_contact_no(self, contact_no):
        self._contact_no = contact_no

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password


class Library:
    def __init__(self):
        self._books = []
        self._librarians = []
        self._members = []

    def get_books(self):
        return self._books

    def set_books(self, books):
        self._books = books

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book_id):
        self._books = [book for book in self._books if book.get_book_id() != book_id]

    def all_books(self):
        for book in self._books:
            print(book.get_book_id(), ":", book.get_book_name())

    def check_librarian(self, id, password):
        for librarian in self._librarians:
            if librarian.get_id() == id and librarian.get_password() == password:
                return True
        return False

    def add_librarian(self, id, name, contact_no, password):
        self._librarians.append(Librarian(id, name, contact_no, password))

    def remove_librarian(self, id):
        self._librarians = [librarian for librarian in self._librarians if librarian.get_id() != id]

    def add_member(self, member):
        self._members.append(member)

    def check_member(self, name, password):
        for member in self._members:
            if member.get_name() == name and member.get_password() == password:
                return member
        return None


class Book:
    book_id_counter = 100

    def __init__(self, book_name, price, author, publication):
        self._book_id = Book.book_id_counter
        Book.book_id_counter += 1
        self._book_name = book_name
        self._price = price
        self._author = author
        self._publication = publication

    def get_book_id(self):
        return self._book_id

    def get_book_name(self):
        return self._book_name

    def set_book_name(self, book_name):
        self._book_name = book_name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_publication(self):
        return self._publication

    def set_publication(self, publication):
        self._publication = publication


class Member:
    def __init__(self, name, contact, m_type, password):
        self._name = name
        self._contact = contact
        self._m_type = m_type
        self._password = password
        self._books_issued = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def get_m_type(self):
        return self._m_type

    def set_m_type(self, m_type):
        self._m_type = m_type

    def get_books_issued(self):
        return self._books_issued

    def set_books_issued(self, books_issued):
        self._books_issued = books_issued

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def issue_book(self, book):
        if len(self._books_issued) < 3:
            self._books_issued.append(book)
        else:
            print("Limit reached: Cannot issue more than 3 books.")

    def return_book(self, book):
        if book in self._books_issued:
            self._books_issued.remove(book)


class Staff(Member):
    def __init__(self, m_id, name, contact, password):
        self.set_name(name)
        self.set_contact(contact)
        self.set_m_type("Staff")
        self.set_password(password)
        self._m_id = m_id

    def get_m_id(self):
        return self._m_id

    def set_m_id(self, m_id):
        self._m_id = m_id


class Student(Member):
    def __init__(self, enr_no, name, contact, password):
        self.set_name(name)
        self.set_contact(contact)
        self.set_m_type("Student")
        self.set_password(password)
        self._fine = 0
        self._enr_no = enr_no

    def get_enr_no(self):
        return self._enr_no

    def set_enr_no(self, enr_no):
        self._enr_no = enr_no

    def get_fine(self):
        return self._fine

    def set_fine(self, fine):
        self._fine = fine

    def pay_fine(self, fine):
        if fine > self._fine:
            print("Given money is more than fine.")
            print(f'Your fine is {self._fine}')
        elif fine < self._fine:
            print(f'Fine paid: {fine}\nRemaining fine: {self._fine - fine}')
            self._fine -= fine
        else:
            print("Fine paid.")
            self._fine = 0


def main():
    lib = Library()
    while True:
        n = int(input("1) Login\n2) Register\n3) Exit\nEnter your choice: "))
        if n == 3:
            break
        ty = int(input("1) Librarian\n2) Staff\n3) Student\n4) Exit\nEnter your choice: "))
        if ty == 4:
            break
        if n == 1:
            if ty == 1:
                id = int(input("Enter your Id: "))
                password = input("Enter your password: ")
                if not lib.check_librarian(id, password):
                    print("Id or Password is Wrong.")
                    continue
                while True:
                    opt = int(input("1) Add book\n2) Remove book\n3) Show all books\n4) Remove account\n5) Exit\nEnter your choice: "))
                    if opt == 1:
                        lib.add_book(Book(input("Enter book name: "), input("Enter price: "), input("Enter author: "), input("Enter publication: ")))
                        print("Book added successfully")
                    elif opt == 2:
                        lib.remove_book(int(input("Enter book id: ")))
                    elif opt == 3:
                        lib.all_books()
                    elif opt == 4:
                        lib.remove_librarian(id)
                        break
                    else:
                        break
            else:
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                member = lib.check_member(name, password)
                if not member:
                    print("Name or Password is Wrong.")
                    continue
                while True:
                    opt = int(input("1) Issue book\n2) Return book\n3) Show issued books\n4) Exit\nEnter your choice: "))
                    if opt == 1:
                        book_id = int(input("Enter book id: "))
                        book = next((b for b in lib.get_books() if b.get_book_id() == book_id), None)
                        if book:
                            member.issue_book(book)
                            print("Book issued successfully")
                        else:
                            print("Book not found")
                    elif opt == 2:
                        book_id = int(input("Enter book id: "))
                        book = next((b for b in member.get_books_issued() if b.get_book_id() == book_id), None)
                        if book:
                            member.return_book(book)
                            print("Book returned successfully")
                        else:
                            print("Book not found")
                    elif opt == 3:
                        for book in member.get_books_issued():
                            print(book.get_book_id(), ":", book.get_book_name())
                    else:
                        break
        elif n == 2:
            if ty == 1:
                id = int(input("Enter your Id: "))
                name = input("Enter your name: ")
                contact_no = input("Enter your contact number: ")
                password = input("Enter your password: ")
                lib.add_librarian(id, name, contact_no, password)
                print("Librarian registered successfully")
            elif ty == 2:
                m_id = int(input("Enter your Member Id: "))
                name = input("Enter your name: ")
                contact = input("Enter your contact number: ")
                password = input("Enter your password: ")
                lib.add_member(Staff(m_id, name, contact, password))
                print("Staff registered successfully")
            elif ty == 3:
                enr_no = int(input("Enter your Enrollment Number: "))
                name = input("Enter your name: ")
                contact = input("Enter your contact number: ")
                password = input("Enter your password: ")
                lib.add_member(Student(enr_no, name, contact, password))
                print("Student registered successfully")


main()