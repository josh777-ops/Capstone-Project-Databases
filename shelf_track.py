import sqlite3

DB_NAME = "ebookstore.db"

def create_tables():
    with sqlite3.connect(DB_NAME) as db:
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS author(
            id INTEGER PRIMARY KEY,
            name TEXT,
            country TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT,
            authorID INTEGER,
            qty INTEGER,
            FOREIGN KEY(authorID) REFERENCES author(id)
        )
        """)

        db.commit()

def populate_tables():
    with sqlite3.connect(DB_NAME) as db:
        cursor = db.cursor()

        authors = [
            (1290, "Charles Dickens", "England"),
            (8937, "J.K. Rowling", "England"),
            (2356, "C.S. Lewis", "Ireland"),
            (6380, "J.R.R. Tolkien", "South Africa"),
            (5620, "Lewis Carroll", "England")
        ]

        books = [
            (3001, "A Tale of Two Cities", 1290, 30),
            (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
            (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice’s Adventures in Wonderland", 5620, 12)
        ]

        cursor.executemany("INSERT OR IGNORE INTO author VALUES (?, ?, ?)", authors)
        cursor.executemany("INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)", books)

        db.commit()

def enter_book():
    try:
        book_id = int(input("Enter book ID (4 digits): "))
        title = input("Enter book title: ")
        author_id = int(input("Enter author ID: "))
        qty = int(input("Enter quantity: "))

        with sqlite3.connect(DB_NAME) as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO book VALUES (?, ?, ?, ?)",
                (book_id, title, author_id, qty)
            )
            db.commit()

        print("Book added successfully.")

    except Exception as e:
        print("Error:", e)


def update_book():
    try:
        book_id = int(input("Enter book ID to update: "))

        with sqlite3.connect(DB_NAME) as db:
            cursor = db.cursor()

            cursor.execute("SELECT * FROM book WHERE id=?", (book_id,))
            book = cursor.fetchone()

            if not book:
                print("Book not found.")
                return

            print("1. Update quantity")
            print("2. Update title")
            print("3. Update authorID")

            choice = input("Choose option: ")

            if choice == "1":
                qty = int(input("Enter new quantity: "))
                cursor.execute("UPDATE book SET qty=? WHERE id=?", (qty, book_id))

            elif choice == "2":
                title = input("Enter new title: ")
                cursor.execute("UPDATE book SET title=? WHERE id=?", (title, book_id))

            elif choice == "3":
                author_id = int(input("Enter new author ID: "))
                cursor.execute("UPDATE book SET authorID=? WHERE id=?", (author_id, book_id))

            db.commit()
            print("Book updated.")

    except Exception as e:
        print("Error:", e)


def delete_book():
    try:
        book_id = int(input("Enter book ID to delete: "))

        with sqlite3.connect(DB_NAME) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM book WHERE id=?", (book_id,))
            db.commit()

        print("Book deleted.")

    except Exception as e:
        print("Error:", e)


def search_book():
    try:
        title = input("Enter title to search: ")

        with sqlite3.connect(DB_NAME) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + title + '%',))

            results = cursor.fetchall()

            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")

    except Exception as e:
        print("Error:", e)


def view_books():
    with sqlite3.connect(DB_NAME) as db:
        cursor = db.cursor()

        cursor.execute("""
        SELECT book.title, author.name, author.country
        FROM book
        INNER JOIN author
        ON book.authorID = author.id
        """)

        results = cursor.fetchall()

        print("\nDetails")
        print("-" * 40)

        for title, name, country in results:
            print(f"Title: {title}")
            print(f"Author's Name: {name}")
            print(f"Author's Country: {country}")
            print("-" * 40)

def menu():
    while True:
        print("\nBookstore Menu")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("5. View details of all books")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            enter_book()

        elif choice == "2":
            update_book()

        elif choice == "3":
            delete_book()

        elif choice == "4":
            search_book()

        elif choice == "5":
            view_books()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

create_tables()
populate_tables()
menu()