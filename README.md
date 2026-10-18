# Student Record Management System

**Course:** PROG211 – Object-Oriented Programming 1  
**Project Domain:** Education  
**Programming Language:** Python 3

## 1. Project Overview

The Student Record Management System is a menu-driven Python application developed to manage student information and academic results. The system allows users to register students, search for student records, display students by course, record academic results, and retrieve results by student ID, grade, or subject.

The project demonstrates object-oriented programming, data structures, methods, input validation, and selected Digital Public Goods (DPG) principles.

## 2. Project Objectives

The objectives of this project are to:

- Apply object-oriented programming concepts in Python.
- Create classes and objects to represent students and academic results.
- Use a dictionary to manage student records.
- Use a list to store academic results.
- Implement instance methods, a static method, and a class method.
- Validate user input and prevent duplicate student IDs.
- Demonstrate modularity, accessibility considerations, and privacy awareness.

## 3. System Features

The system provides the following functions:

1. Register a student.
2. Display all registered students.
3. Search for a student by ID.
4. Count registered students.
5. Display student names and IDs.
6. Display students by course.
7. Add a student's academic result.
8. Display all recorded results.
9. Display results by student ID.
10. Display results by grade.
11. Display results by subject.
12. Count recorded results.
13. Exit the application.

## 4. Object-Oriented Design

### 4.1 Student Class

The `Student` class represents an individual student. It stores the student's ID, name, and course. Its methods display student information, update a student's course, and retrieve individual student details.

### 4.2 StudentRegistry Class

The `StudentRegistry` class manages student objects using a dictionary. It supports student registration, searching, displaying records, filtering students by course, and counting students. It also contains a static method for validating student details and a class method for retrieving the total registered count.

### 4.3 Result Class

The `Result` class represents an academic result. It stores the student ID, subject, mark, and grade. Its methods display and retrieve result information.

### 4.4 ResultRegistry Class

The `ResultRegistry` class manages result objects using a list. It supports adding results, displaying all results, searching by student ID, filtering by grade or subject, and counting recorded results.

## 5. Data Structures

**Dictionary:** The `StudentRegistry` class uses a dictionary to store student objects. Each student ID acts as a unique key, allowing records to be retrieved efficiently and duplicate IDs to be checked.

**List:** The `ResultRegistry` class uses a list to store multiple result objects. Each result contains the associated student ID, subject, mark, and grade.

## 6. Input Validation

The application checks that required student details are not empty and prevents the registration of duplicate student IDs. It also validates marks to ensure that they are numeric and fall between 0 and 100.

When recording a result, the system checks that the student ID belongs to a registered student.

## 7. How to Run the Program

### Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor

No external Python packages are required.

### Instructions

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Run the Python file.
5. Select a menu option by entering its number in the terminal.
6. Follow the prompts to register students, search records, and manage academic results.

## 8. Example Usage

The following example illustrates how a student can be registered:

**Input:**

- Student ID: ST001
- Student Name: Francess Glennis
- Course: Business Information Technology

**Expected output:**

`Student registered successfully.`

When the user selects the option to display all students, the application displays each registered student's ID, name, and course.

When the user records an academic result, the application requests the student ID, subject, mark, and grade. The saved result can then be displayed or searched using the available menu options.

## 9. Digital Public Goods Principles

### 9.1 Open Source

The application is written in Python and its source code can be shared and inspected. Permissions for reuse and modification depend on the licence selected for the repository.

### 9.2 Inclusion and Accessibility

The text-based menu provides a straightforward way to interact with the application using a keyboard and terminal. Additional improvements may be required to support users with different accessibility needs.

### 9.3 Privacy

The application does not require online accounts or send student information to an external service. However, users should avoid exposing real student information in public demonstrations or repositories.

### 9.4 Modularity and Reusability

The program separates student information, student registration, academic results, and result management into different classes. This structure supports maintenance, testing, and future extension.

This project demonstrates selected principles associated with Digital Public Goods. It has not been formally certified or recognised as a Digital Public Good.

## 10. Limitations

The application stores student records and results in memory while the program is running. The information is lost when the program closes because permanent file or database storage has not been implemented.

Grades are entered manually and are not automatically calculated from marks. The current application also does not include user authentication or a graphical user interface.

## 11. Future Improvements

Possible improvements include:

- Implementing permanent storage using a database or file.
- Calculating grades automatically from marks.
- Adding user authentication and access controls.
- Developing a graphical user interface.
- Adding functions to edit and delete student records and results.

## 12. Conclusion

The Student Record Management System demonstrates the practical application of object-oriented programming, dictionaries, lists, methods, and input validation in Python. It provides basic student and academic result management features and offers a foundation for future development.