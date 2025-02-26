from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://bvjv656:vbfTSR78a6ASozFe@cluster0.6rh0n.mongodb.net/Library?retryWrites=true&w=majority")
        self.db = self.client["LibrarySystem"]
        self.books = self.db["Books"]
        self.librarians = self.db["Librarians"]
        self.members = self.db["Members"]

    def insert(self, collection, data):
        return self.db[collection].insert_one(data).inserted_id

    def find(self, collection, query):
        return self.db[collection].find_one(query)

    def find_all(self, collection):
        return list(self.db[collection].find())

    def delete(self, collection, query):
        self.db[collection].delete_one(query)

class Librarian:
    def __init__(self, db, id, name, contact_no, password):
        self.db = db
        self.id = id
        self.name = name
        self.contact_no = contact_no
        self.password = password
        self.db.insert("Librarians", self.__dict__)

class Book:
    def __init__(self, db, book_name, price, author, publication):
        self.db = db
        self.book_name = book_name
        self.price = price
        self.author = author
        self.publication = publication
        self.db.insert("Books", self.__dict__)

class Member:
    def __init__(self, db, name, contact, m_type, password):
        self.db = db
        self.name = name
        self.contact = contact
        self.m_type = m_type
        self.password = password
        self.books_issued = []
        data = {k: v for k, v in self.__dict__.items() if k != "db"}
        self.db.insert("Members", data)


    def issue_book(self, book_name):
        if len(self.books_issued) < 3:
            self.books_issued.append(book_name)
            self.db.db["Members"].update_one({"name": self.name}, {"$set": {"books_issued": self.books_issued}})
        else:
            print("Cannot issue more than 3 books.")

    def return_book(self, book_name):
        if book_name in self.books_issued:
            self.books_issued.remove(book_name)
            self.db.db["Members"].update_one({"name": self.name}, {"$set": {"books_issued": self.books_issued}})

class Library:
    def __init__(self):
        self.db = Database()

    def add_book(self, book_name, price, author, publication):
        Book(self.db, book_name, price, author, publication)

    def remove_book(self, book_name):
        self.db.delete("Books", {"book_name": book_name})

    def list_books(self):
        for book in self.db.find_all("Books"):
            print(book["book_name"], "by", book["author"])

    def add_librarian(self, id, name, contact_no, password):
        Librarian(self.db, id, name, contact_no, password)

    def authenticate_librarian(self, id, password):
        return self.db.find("Librarians", {"id": id, "password": password})

    def register_member(self, name, contact, m_type, password):
        Member(self.db, name, contact, m_type, password)

    def authenticate_member(self, name, password):
        return self.db.find("Members", {"name": name, "password": password})

def main():
    library = Library()
    while True:
        choice = int(input("1) Login\n2) Register\n3) Exit\nEnter choice: "))
        if choice == 3:
            break
        role = int(input("1) Librarian\n2) Member\nEnter choice: "))
        if choice == 1:
            name = input("Enter name: ")
            password = input("Enter password: ")
            if library.authenticate_member(name, password):
                print("Login successful!")
            else:
                print("Invalid credentials.")
        elif choice == 2:
            name = input("Enter name: ")
            contact = input("Enter contact: ")
            m_type = input("Enter type (Student/Staff): ")
            password = input("Enter password: ")
            library.register_member(name, contact, m_type, password)
            print("Member registered successfully!")

if __name__ == "__main__":
    main()
