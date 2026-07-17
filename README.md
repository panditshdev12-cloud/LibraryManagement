# Library Management System

## Project Purpose

The Library Management System is a Python-based application developed to help manage the daily operations of a library. The system allows users to manage books, library members, borrowing activities, and transaction records through an interactive menu-driven interface.

The purpose of this project is to demonstrate fundamental Python programming concepts, including object-oriented programming, classes and objects, file handling, exception handling, and modular software development.

The system provides an organized way to store and manage library information while reducing manual record management.

---

## Features

The application provides the following features:

- Add new books to the library
- View all available books
- Search books by title or author
- Remove books from the system
- Register new library members
- View member information
- Remove members
- Borrow books
- Return books
- Track borrowing and return transactions
- Generate library reports
- Store data permanently using CSV files
- Automatically load existing data when the program starts
- Automatically save changes during operations
- Handle invalid operations using exception handling

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- CSV File Handling
- Python Modules and Packages

---

## Project Structure

```
library_management_system/

├── main.py

├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   └── transaction.py

├── services/
│   ├── __init__.py
│   └── library.py

├── utils/
│   ├── __init__.py
│   └── file_handler.py

├── data/
│   ├── books.csv
│   ├── members.csv
│   └── transactions.csv
```

---

## Installation and Execution

### Requirements

- Python 3.x installed on the computer

### Running the Application

1. Download or clone the project repository.

2. Open the project folder in a terminal or Visual Studio Code.

3. Run the following command:

```
python main.py
```

4. The application menu will appear, allowing the user to interact with the library system.

---

## Example Usage

When the program starts, the user will see a menu:

```
==============================
 LIBRARY MANAGEMENT SYSTEM
==============================

1. Book Management
2. Member Management
3. Borrow Book
4. Return Book
5. View Transactions
6. Reports
7. Save and Exit
```

Example of borrowing a book:

```
Enter choice: 3

Member ID: M001
Book ID: B001

Book borrowed successfully.
```

The transaction will automatically be stored in the transaction history file.

---

## Data Storage

The system uses CSV files to store information permanently.

### books.csv

Stores information about all books, including:

- Book ID
- Title
- Author
- Genre
- ISBN
- Publication year
- Availability status

### members.csv

Stores information about library members, including:

- Member ID
- Name
- Email
- Phone number
- Borrowed books

### transactions.csv

Stores borrowing and returning records, including:

- Transaction ID
- Member ID
- Book ID
- Action type
- Date and time

---

## Object-Oriented Design

The project is divided into several classes:

### Book Class

Represents books in the library and manages book information.

### Member Class

Represents library users and tracks borrowed books.

### Transaction Class

Records borrowing and returning activities.

### Library Class

Acts as the main controller and manages books, members, transactions, and file operations.

---

## Error Handling

The application includes error handling to prevent crashes and manage unexpected situations, such as:

- Invalid menu choices
- Missing files
- Duplicate book or member IDs
- Invalid borrowing or returning operations

---

## Future Improvements

Possible future improvements include:

- Adding a graphical user interface (GUI)
- Connecting the system to a database
- Adding user authentication
- Creating advanced search filters
- Generating downloadable reports

---

## Author

Library Management System developed as a Python programming project.