# Capstone-Project-Databases

# 📚 Shelf Track – Bookstore Inventory Management System

## Overview

Shelf Track is a Python and SQLite database application developed as a capstone project for the HyperionDev Databases module. The application provides a simple command-line interface (CLI) that allows bookstore staff to manage book inventory efficiently.

The project demonstrates the use of Python programming, SQL, SQLite databases, relational database design, modular programming, error handling, input validation, and database management best practices.

---

## Features

The application allows users to:

* ➕ Add new books to the inventory
* ✏️ Update existing book information
* 🗑️ Delete books from the database
* 🔍 Search for books by ID
* 📖 View details of all books, including:

  * Book title
  * Author name
  * Author country

---

## Database Structure

The project uses an SQLite database named **ebookstore.db**.

### Book Table

| Column   | Description                            |
| -------- | -------------------------------------- |
| id       | Book ID (Primary Key)                  |
| title    | Book title                             |
| authorID | Foreign key linked to the Author table |
| qty      | Number of books in stock               |

### Author Table

| Column  | Description             |
| ------- | ----------------------- |
| id      | Author ID (Primary Key) |
| name    | Author's full name      |
| country | Author's country        |

The two tables are connected using a foreign key relationship:

book.authorID → author.id

---

## Technologies Used

* Python 3
* SQLite3
* SQL
* Command Line Interface (CLI)

---

## Project Structure

```text
Shelf_Track/
│
├── shelf_track.py          # Main application
├── ebookstore.db           # SQLite database
├── README.md               # Project documentation
└── requirements.txt        # (Optional)
```

---

## Menu Options

```text
1. Enter Book
2. Update Book
3. Delete Book
4. Search Books
5. View Details of All Books
0. Exit
```

---

## Key Concepts Demonstrated

* SQLite database creation
* SQL CRUD operations
* Relational databases
* INNER JOIN queries
* Foreign keys
* Python functions (modularity)
* Exception handling
* Data validation
* Context managers (`with` statements)
* Clean code principles
* User-friendly CLI design

---

## Input Validation

The application validates user input by:

* Ensuring Book IDs and Author IDs are numeric.
* Checking ID length requirements.
* Preventing invalid or empty inputs.
* Handling database errors gracefully.
* Using parameterized SQL queries to help protect against SQL injection.

---

## Example Output

```text
Details
--------------------------------------------------

Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling
Country: England

--------------------------------------------------

Title: The Lord of the Rings
Author: J.R.R. Tolkien
Country: South Africa
```

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Python programming
* Database design
* SQL queries
* CRUD operations
* Database relationships
* Code refactoring
* Software engineering best practices
* Problem solving and debugging

---

## Future Improvements

Potential enhancements include:

* Search books by title or author
* Sort books alphabetically
* Export inventory to CSV
* Add categories or genres
* Build a graphical user interface (GUI)
* Add user authentication
* Support multiple bookstore branches

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/shelf-track.git
```

Navigate into the project directory:

```bash
cd shelf-track
```

Run the application:

```bash
python shelf_track.py
```

---

## Author

Developed as part of the **HyperionDev Software Engineering Bootcamp** Capstone Project.

---

## License

This project is intended for educational and portfolio purposes.
