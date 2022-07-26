BOOKLIST = 'Books.txt'


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print(f"Books present in this library are:\n {self.books} ")

        for index, book in enumerate(self.books):
            print(index + 1, book)

    def allBooks(self):
        with open('Books.txt', "w+") as f:
            availabe_books = f.write(str(self.books))

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):

        self.book = input("Enter the name of the book you want to borrow: ").lower()
        return self.book

    def returnBook(self):

        self.book = input("Enter the name of the book you want to return: ").lower()
        return self.book


if __name__ == "__main__":
    kamleshLibrary = Library(["Rich dad Poor dad", "Think and Grow Rich", "The power of your subconsicious mind", "How to influence people",
                             "Time management", "Alchemist", "Intelligent Investor", "Atomic habits", "ikigai", "Questions are answers", "babylon's richest man"])
    student = Student()
    kamleshLibrary.allBooks()
    # centraLibrary.displayAvailableBooks()
    welcomeMsg = '''\n ====== Welcome to Kamlesh Library ======
    Please choose an option:
    1. List all the books
    2. Request a book
    3. Add/Return a book
    4. Exit the Library
    '''
    print(welcomeMsg)
    while(True):
        try:
            a = int(input("Enter a choice: "))
            if a == 1:
                kamleshLibrary.displayAvailableBooks()
            elif a == 2:
                kamleshLibrary.borrowBook(student.requestBook())
            elif a == 3:
                kamleshLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for choosing Central Library. Have a great day ahead!")
                exit()
            else:
                print("Invalid Choice!")
        except Exception as e:
            print("Make sure you have enter a valid word")
