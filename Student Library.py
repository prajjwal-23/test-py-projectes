class library:
    def __init__(self, listofbooks):
        self.books = listofbooks
    
    def displayavailablebook(self):
        print("Books present in library are: ")
        for book in self.books:
            print(" *"+book)
    
    def BorrowBooks(self , Bookname):
        if Bookname in self.books:
            print(f"You have been issued {Bookname}. Please keep it safe and return it with in 30 days.")
            self.books.remove(Bookname)
        else:
            print("Sorry, this book is not available or already issued to someone else, Please wait until the book is available. ")

    def returnBook(self, Bookname) :
        self.books.append(Bookname)
        print('Thanks for returnig the book.')

class student:
    def requestBook(self):
        self.book = input("Enter book name that u want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book that you want to return: ")
        return self.book
    
if __name__ == "__main__":
    centralLibrary = library(["Algorithems","Math Matics","Chemistry","Python","c programming"])
    student = student()
    while(True):
        welcomeMsg = ''' ****** Welcome to central Library ******
        Please chose an option
        1. List all the books 
        2. Request a book 
        3. Return a book
        4. Exit the library
        '''
        try:                
            print(welcomeMsg)
            a = int(input("Enter a choice: "))

        except:
            print('\n**Please input a vailid value**\n')
            continue
        if a == 1:
            centralLibrary.displayavailablebook()
        elif a == 2:
            centralLibrary.BorrowBooks(student.requestBook())
        elif a ==3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead! ")
            exit()
        else:
            print("invailid choice")
