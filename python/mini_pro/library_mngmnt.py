import json
class Library:
    def __init__(self):
        self.books = {}
        self.load_from_file()

    def add_book(self, book_title, author, price):
        try:
            if book_title not in self.books:
                self.books[book_title] = {'author': author, 'price': price}
                print(f"Book '{book_title}' by {author} added to the library. Price: ₹{price:.2f}")
            else:
                print(f"Book '{book_title}' is already in the library.")
        except:
            print("An error occurred")

    def display_books(self):
        try:
            if not self.books:
                print("The library is empty.")
            else:
                print("\nLibrary Books:")
                for title, info in self.books.items():
                    print(f"{title} by {info['author']} - Price: ₹{info['price']:.2f}")
        except:
            print("An error occurred")

    def search_book(self, book_title):
        try:
            if book_title in self.books:
                info = self.books[book_title]
                print(f"Book '{book_title}' is available in the library. Author: {info['author']} - Price: ₹{info['price']:.2f}")
            else:
                print(f"Book '{book_title}' is not in the library.")
        except:
            print("An error occurred")

    def remove_book(self, book_title):
        try:
            if book_title in self.books:
                del self.books[book_title]
                print(f"Book '{book_title}' removed from the library.")
            else:
                print(f"Book '{book_title}' is not in the library.")
        except:
            print("An error occurred")

    def save_to_file(self):
        try:
            with open("../PYTHON/mini_pro/libdata.json", 'w') as file:
                json.dump(self.books, file, indent=3)
            print("Library data saved to file 'library_data.json'")
        except:
            print("An error occurred while saving to file")

    def load_from_file(self):
        try:
            with open("../PYTHON/mini_pro/libdata.json", 'r') as file:
                self.books = json.load(file)
            print("Library data loaded from file 'library_data.json'")
        except FileNotFoundError:
            print("No existing library data file found. Starting with an empty library.")
        except:
            print(f"An error occurred while loading from file")


obj = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Quit")

    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the title of the book: ").lower()
        author = input("Enter the author of the book: ").lower()
        price = float(input("Enter the price of the book: ₹"))
        obj.add_book(title, author, price)

    elif choice == '2':
        obj.display_books()

    elif choice == '3':
        title = input("Enter the title of the book to search: ").lower()
        obj.search_book(title)

    elif choice == '4':
        title = input("Enter the title of the book to remove: ").lower()
        obj.remove_book(title)

    elif choice == '5':
        obj.save_to_file()
        print("Thank You So Much")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    dywtc = input("Do you want to Continue? (y/n): ")
    if dywtc.lower() == 'n'or dywtc.lower() != 'y':
        obj.save_to_file()
        print("Thank You So Much")
        break