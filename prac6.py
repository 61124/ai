books = [
    {"title":"Sherlock Holmes","author":"Arthur Conan Doyle","available":True,"genre":"Mystery"},
    {"title": "Python Programming", "author": "Reema Thareja", "available": True, "genre": "Technology"},
    {"title": "Data Science 101", "author": "Rajendra Verma", "available": False, "genre": "Science"},
    {"title": "Machine Learning Basics", "author": "James Brown", "available": True, "genre": "Technology"},
    {"title": "Quantum Physics", "author": "Arnold Digger", "available": True, "genre": "Science"},
    {"title": "History of Literature", "author": "Louisa Alcott", "available": True, "genre": "Literature"},
    {"title": "Pride and Prejudice", "author": "Roald Dahl", "available": False, "genre": "Literature"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "available": True, "genre": "Science"},
    {"title": "Steve Jobs", "author": "Walter Isaacson", "available": False, "genre": "Biography"},
    {"title": "Harry Potter", "author": "J.K. Rowling", "available": True, "genre": "Fantasy"},
    {"title": "The Art of War", "author": "Sun Tzu", "available": True, "genre": "History"},
    {"title": "The Republic", "author": "Plato", "available": False, "genre": "Philosophy"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True, "genre": "Fiction"}
]

def check_availability(title):
    for book in books:
        if title.lower() == book["title"].lower():
            return book["available"]
    return False

def get_recommendation(genre):
    result = []
    for book in books:
        if book["genre"].lower()==genre.lower():
            result.append(book["title"])
    return result

def list_books():
    for book in books:
        if book["available"]:
            status = "Available"
        else:
            status = "Not available"
        print("Title:",book["title"],"by",book["author"],"Genre:",book["genre"],"Availability:",status)
        
print("Welcome to library information system!")
while True:
    print("\nOptions:\n1. Check book availability\n2. Recommend books by genre\n3. List all books\n4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        title = input("Enter book title: ")
        available = check_availability(title)
        if available is True:
            print("Yes, the book is available.")
        elif available is False:
            print("The book is not available.")
        else:
            print("Book not found.")
    elif choice == '2':
        genre = input("Enter genre: ")
        recs = get_recommendation(genre)
        if recs:
            print("\nRecommended books:")
            for b in recs:
                print(b)
        else:
            print("No available books in that genre.")
    elif choice == '3':
        print("\nAll books in the library:")
        list_books()
    elif choice == '4':
        print("Goodbye!")
        break    
    else:
        print("Invalid choice. Try again.")