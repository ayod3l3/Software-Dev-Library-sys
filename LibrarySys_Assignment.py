import re
import uuid
from datetime import datetime, timedelta

#Define the Book class
class Book:
    def __init__(self):
        #Initialize Book properties
        self.book_id = str(uuid.uuid4())  #Generate a random UUID as the book ID
        self.title = None
        self.author = None
        self.year = None
        self.publisher = None
        self.total_copies = None
        self.available_copies = None
        self.publication_date = None

#Define set methods to assign values to Book properties
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_total_copies(self, total_copies):
        self.total_copies = total_copies
        self.available_copies = total_copies

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

#Define get methods to retrieve values of book properties
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_total_copies(self):
        return self.total_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date

#Define method to display Book details
    def display_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Publisher:", self.publisher)
        print("Total Copies:", self.total_copies)
        print("Available Copies:", self.available_copies)
        print("Publication Date:", self.publication_date)
        print("")  # Print an empty line for readability

#Define the BookList class
class BookList:
    def __init__(self):
        self.collection = {}

#Define method as a dictionary to store book instances
    def store_book(self, book):
        self.collection[book.get_title()] = book

#Define search method using title, author, publisher or publication date
    def search_book(self, search_key, search_value):
        search_results = []

        for book in self.collection.values():
            if (
                search_key == "title" and search_value in book.get_title() or
                search_key == "author" and search_value in book.get_author() or
                search_key == "publisher" and search_value in book.get_publisher() or
                search_key == "publication_date" and search_value == str(book.get_publication_date())
            ):
                search_results.append(book)

        return search_results

#Define method to remove a Book from the collection
    def remove_book(self, title):
        if title in self.collection:
            del self.collection[title]
            print(f"Book '{title}' has been removed from the collection.")
        else:
            raise ValueError("Book not found in the collection")

#Define method to get the total number of Books in the collection
    def get_total_books(self):
        return len(self.collection)

#Define the User class
class User:
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, dob):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

 #Define get methods to retrieve User properties
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

#Define methods to edit User details
    def edit_firstname(self, new_firstname):
        self.firstname = new_firstname

    def edit_surname(self, new_surname):
        self.surname = new_surname

    def edit_email(self, new_email):
        if self.is_valid_email(new_email):
            self.email = new_email
        else:
            raise ValueError("Invalid email address format")

    def edit_dob(self, new_dob):
        if self.is_valid_date(new_dob):
            self.dob = new_dob
        else:
            raise ValueError("Invalid date of birth format")

# Define methods for validating email and date formats
    def is_valid_email(self, email):
        # Regex for validation of email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # If email passes validation pattern
        if re.match(regex, email):
            return True
        else:
            return False

    def is_valid_date(self, date):
        try:
            datetime.strptime(date, "%d-%m-%y")
            return True
        except ValueError:
            return False

#Define the UserList class
class UserList:
    def __init__(self):
        self.collection = {} #define method as a dictionary for user instances created with class Users.

    def store_user(self, user):
        self.collection[user.get_username()] = user
        
#define method to remove user by using firstname and indicate multiple users with same firstname 
    def remove_user_by_first_name(self, first_name):
        usernames_to_remove = [username for username,\
        user in self.collection.items() if user.get_firstname() == first_name]

        if len(usernames_to_remove) == 0:
            print(f"No users found with the first name {first_name}")
        elif len(usernames_to_remove) == 1:
            del self.collection[usernames_to_remove[0]]
            print(f"User with the first name {first_name} has been successfully removed.")
            
        else:
            print(f"Multiple users found with the first name {first_name}. Specify a username to remove.")
            specified_username = input("Enter the username of the user to be remove: ")
            if specified_username in self.collection:
                del self.collection[specified_username]
                print(f"User with username {specified_username} has been successfully removed.")
            else:
                print(f"User with username {specified_username} not found in the collection.")

#Define method to count the number of Users in the collection
    def count_users(self):
        return len(self.collection)

#Define method to get User details by username
    def get_user_details(self, username):
        if username in self.collection:
            return self.collection[username]
        else:
            raise ValueError("User not found in the collection")

# Define the Loan class
class Loan:
    def __init__(self):
        self.loans = {}
        
#Define a method for user to borrow a book and assign book to user
    def borrow_book(self, user, book):
        if book.get_available_copies() == 0:
            raise ValueError("No available copies of the book")
        self.loans[book] = user
        book.available_copies -= 1
        
# Define method to return books by user and un-assign borrowed book from user
    def return_book(self, book):
        if book in self.loans:
            del self.loans[book]
        else:
            raise ValueError("Book not found in the loan records")
        
#Define the number of books a user has borrowed 
    def count_borrowed_books(self, user):
        count = sum(1 for borrowed_user in self.loans.values() if borrowed_user == user)
        return count
    
#Display overdue books, username and firstname of user
    def get_overdue_books(self, user_list):
        current_date = datetime.now().date()
        overdue_books = []

        for book, borrowed_user in self.loans.items():
            due_date = current_date + timedelta(days=14)  #With a 14-day book loan period
            if current_date > due_date:
                overdue_books.append((book, borrowed_user))

        for book, user in overdue_books:
            username = user.get_username()
            first_name = user.get_firstname()
            print(f"Overdue Book: {book.get_title()} (Username: {username}, First Name: {first_name})")

# Create Library System instance
class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loan_system = Loan()

 #Define methods to interact with BookList, UserList, and Loan
    def add_book(self, book):
        self.book_list.store_book(book)

    def add_user(self, user):
        self.user_list.store_user(user)

    def borrow_book(self, username, book_title):
        user = self.user_list.get_user_details(username)
        book = self.book_list.search_book("title", book_title)[0]
        self.loan_system.borrow_book(user, book)

    def return_book(self, username, book_title):
        user = self.user_list.get_user_details(username)
        book = self.book_list.search_book("title", book_title)[0]
        self.loan_system.return_book(book)

    def count_borrowed_books(self, username):
        user = self.user_list.get_user_details(username)
        return self.loan_system.count_borrowed_books(user)

    def get_overdue_books(self):
        self.loan_system.get_overdue_books(self.user_list)

    def search_book_menu(self):
        search_key = input("Enter search key (title, author, publisher, publication_date): ")
        search_value = input("Enter search value: ")

        search_results = self.book_list.search_book(search_key, search_value)

        if search_results:
            print("\nSearch Results:")
            for book in search_results:
                print(f"Book Title: {book.get_title()}")
                print(f"Author: {book.get_author()}")
                print(f"Year: {book.get_year()}")
                print(f"Publisher: {book.get_publisher()}")
                print(f"Total Copies: {book.get_total_copies()}")
                print(f"Available Copies: {book.get_available_copies()}")
                print(f"Publication Date: {book.get_publication_date()}")
                print("")
        else:
            print("No matching books found.")
        
# Extension to program to modify Books and Users details.  
    def modify_book_details(self, book_title):
        book = self.book_list.search_book("title", book_title) #Search book to be modified by title
        if book:
            book = book[0]
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_year = input("Enter new year: ")
            new_publisher = input("Enter new publisher: ")
            new_copies = int(input("Enter new number of copies: "))

            book.set_title(new_title)
            book.set_author(new_author)
            book.set_year(new_year)
            book.set_publisher(new_publisher)
            book.set_total_copies(new_copies)
        else:
            print("Book not found in the collection") #if the title is not found

    def modify_user_details(self, username):
        try:
            user = self.user_list.get_user_details(username) # Search user by username
            if user:
                new_first_name = input("Enter new first name: ")
                new_surname = input("Enter new surname: ")
                new_house_number = input("Enter new house number: ")
                new_street_name = input("Enter new street name: ")
                new_postcode = input("Enter new postcode: ")

                user.edit_firstname(new_first_name)
                user.edit_surname(new_surname)
                user.house_number = new_house_number
                user.street_name = new_street_name
                user.postcode = new_postcode
            else:
                print("User not found in the collection") # If the user name does not exist or is spelt incorrectly

        except ValueError as e:
            print(f"Error: {e}")

#Initialize library system
library = LibrarySystem()

#Add fictitious books details
book1 = Book() 
book1.set_title("How to Win Everyday")
book1.set_author("Thomas Crown")
book1.set_year("1988")
book1.set_publisher("World Publishing Inc")
book1.set_total_copies(15)
book1.set_publication_date("1990")
library.add_book(book1)

book2 = Book()
book2.set_title("To Catch a Stray Dog")
book2.set_author("Tunde Oladele")
book2.set_year("2020")
book2.set_publisher("The Book Publishing Inc")
book2.set_total_copies(10)
book2.set_publication_date("2021")
library.add_book(book2)

book3 = Book()
book3.set_title("10 Powerful Habits of Success")
book3.set_author("Chris Power")
book3.set_year("2016")
book3.set_publisher("Watermarks Publishing")
book3.set_total_copies(17)
book3.set_publication_date("2017")
library.add_book(book3)

# Add some fictitious users with user details
user1 = User("ASmith", "Alice", "Smith", "123", "Main St", "12345", "alice@example.com", "01-01-95")
user2 = User("Alpha1", "John", "Rose", "25", "Plumstead Street", "N1 2T", "johnrose@user.test", "15-02-1987")
user3 = User("LadyJ", "Joy", "Carpenter", "01", "Long Street", "C5 2K", "joyc@user.test", "19-09-2000")
user4 = User("Baller01", "Bentley", "David", "45", "London Street", "J3 23P", "baller@user.test", "01-11-2007")
user5 = User("Alpha", "John", "Bailley", "12", "Livermore Street", "Y1 3L", "johnb@user.test", "23-02-2001")

library.add_user(user1)
library.add_user(user2)
library.add_user(user3)
library.add_user(user4)
library.add_user(user5)



# Menu for user interface

while True:
    print("\n1. Modify Book Details")
    print("2. Modify User Details")
    print("3. Remove User by First Name")
    print("4. Show User Details")
    print("5. Borrow Book") 
    print("6. Return Book") 
    print("7. Count Borrowed Books")
    print("8. Show Overdue Books")
    print("9. Count Number of Users")
    print("10. Search Book")
    print("11. Remove Book")
    print("12. Total Number of Books")
    print("13. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        book_title = input("Enter the title of the book to modify: ")
        library.modify_book_details(book_title)
    elif choice == "2":
        username = input("Enter the username of the user to modify: ")
        library.modify_user_details(username)
    elif choice == "3":
        first_name = input("Enter the first name of the user to remove: ")
        library.user_list.remove_user_by_first_name(first_name)
    elif choice == "4":
        username = input("Enter the username of the user: ")
        user_details = library.user_list.get_user_details(username)
        if user_details:
            print("User Details:")
            print(f"Username: {user_details.get_username()}")
            print(f"Full Name: {user_details.get_firstname()} {user_details.get_surname()}")
            print(f"Address: {user_details.get_house_number()} {user_details.get_street_name()}, {user_details.get_postcode()}")
            print(f"Email Address: {user_details.get_email()}")
            print(f"Date of Birth: {user_details.get_dob()}")
        else:
            print(f"No user found with the username '{username}'")
    elif choice == "5":
        username = input("Enter your username: ")
        book_title = input("Enter the title of the book to borrow: ")
        library.borrow_book(username, book_title)
    elif choice == "6":
        username = input("Enter your username: ")
        book_title = input("Enter the title of the book to return: ")
        library.return_book(username, book_title)
    elif choice == "7":
        username = input("Enter your username: ")
        borrowed_count = library.count_borrowed_books(username)
        print(f"You are currently borrowing {borrowed_count} book(s).")
    elif choice == "8":
        library.get_overdue_books()
    elif choice == "9":
        user_count = library.user_list.count_users()
        print(f"Number of users in the system: {user_count}")
    elif choice == "10":
        library.search_book_menu()
    elif choice == "11":
        book_title = input("Enter the title of the book to remove: ")
        library.book_list.remove_book(book_title)
    elif choice == "12":
        library.total_books_menu()
    elif choice == "13":
        break
    else:
        print("Invalid choice. Please select again.")
