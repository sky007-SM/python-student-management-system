# Python Student Management System

A command-line student management application written in Python that allows users to manage student records, create courses, assign students to courses, search and sort records, update or delete student information, and persist all data through text-file storage.

## Features

* Add new students
* Add new courses
* Automatically assign unique student IDs
* Store student name, age, and grade
* Store course code, course name, and course credits
* Assign students to courses
* View all student records
* View enrolled courses for each student
* View all course records
* Admin view for enrolled student IDs using an access key
* Search students by ID
* Search students by name
* Update student grades
* Delete student records
* Automatically remove deleted students from enrolled courses
* Sort students by ID
* Sort students by name
* Sort students by age
* Sort students by grade
* Sort courses by course code
* Sort courses by course name
* Sort courses by course credits
* Persistent file-based storage
* Data validation using regular expressions
* Corrupted record filtering and recovery
* Duplicate student ID detection and removal
* Object-Oriented Design
* Class-based alternative constructors using `@classmethod`
* Menu-driven interface

## Concepts Used

* Classes and Objects
* Object-Oriented Programming (OOP)
* Constructors (`__init__`)
* Instance Methods
* Class Methods (`@classmethod`)
* Encapsulation
* Lists
* Nested Lists
* Strings
* File Handling
* Type Hinting
* `Self` Type
* Constants
* Loops
* Conditional Statements
* User Input Handling
* Input Validation
* Exception Handling
* Regular Expressions (`re.search`)
* Lambda Functions
* Sorting with Custom Keys
* Object Serialization and Deserialization

## Run

```bash
python3 main.py
```

## Student Record Format

```text
STUDENT_ID : NAME : AGE : GRADE
```

### Example

```text
1 : Alice Johnson : 16 : 10A
2 : Rahul Sharma : 15 : 9B
3 : Emma Davis : 17 : 11C
```

## Course Record Format

```text
COURSE_CODE | COURSE_NAME | COURSE_CREDITS
```

### Example

```text
CS101 | Computer Science | 4
MTH201 | Mathematics | 5
PHY101 | Physics | 4
```

Student IDs enrolled in each course are stored immediately below the corresponding course record.

Example:

```text
CS101 | Computer Science | 4
1
2
5
```

## Menu Options

| Option | Description |
| ------ | ----------- |
| 1 | Add Student |
| 2 | Add Course |
| 3 | Assign Course |
| 4 | View Students |
| 5 | View Courses |
| 6 | Search Student |
| 7 | Sort Records |
| 8 | Update or Delete Record |
| q | Quit Application |

## Search Capabilities

Students can be searched using:

* Student ID
* Student Name

Search results display all matching records.

## Sorting Capabilities

### Students

Students can be sorted by:

* Student ID
* Student Name
* Student Age
* Student Grade

### Courses

Courses can be sorted by:

* Course Code
* Course Name
* Course Credits

The application uses lambda expressions and custom sorting keys to organize records.

## Course Assignment

Students can be enrolled into existing courses.

Features include:

* Prevents duplicate course enrollment
* Validates course existence
* Maintains enrolled student IDs for every course

Example:

```text
Choose Student and Course

Student ID: 2
Course Name: Computer Science

Student enrolled successfully.
```

## Student Record Updates

Existing student records can be modified.

### Update Grade

Example:

```text
Student ID: 3

Previous Grade: 10B
Updated Grade: 11A
```

### Delete Student

When a student is deleted:

* Student record is removed
* Student ID is removed from every enrolled course
* Remaining records remain intact

## Admin Course View

Course records can be viewed normally by every user.

Entering the administrator access key displays the list of enrolled student IDs for every course.

Example:

```text
CS101 | Computer Science | 4

Students Present by ID:
    [1, 3, 5]
```

## File Structure

```text
file-manager/
└── text-files/
    └── school.txt
```

## Data Storage

The application stores both student records and course records inside a plain text file using the following format:

```text
STUDENT_ID || NAME || AGE || GRADE

COURSE_CODE || COURSE_NAME || COURSE_CREDITS
```

Student IDs enrolled in each course are written beneath their corresponding course record.

All data is automatically saved when the application exits.

## Data Integrity & Recovery

The application validates stored student and course records using regular expressions before loading them into memory.

If the storage file is manually edited, partially corrupted, or contains invalid records:

* Invalid records are ignored automatically
* Valid student records are preserved
* Valid course records are preserved
* Duplicate student IDs are removed
* Recoverable records remain accessible
* Only valid entries are loaded into the management system

This allows the system to continue operating even when the storage file contains damaged or malformed entries.

### Example

Corrupted file:

```text
STUDENT_ID || NAME || AGE || GRADE

1 : Alice Johnson : 16 : 10A
INVALID RECORD
2 : Rahul Sharma : 15 : 9B
BROKEN DATA

COURSE_CODE || COURSE_NAME || COURSE_CREDITS

CS101 | Computer Science | 4
1
2
INVALID ENTRY
```

Recovered records:

```text
1 : Alice Johnson : 16 : 10A
2 : Rahul Sharma : 15 : 9B

CS101 | Computer Science | 4
1
2
```

## Object-Oriented Design

### Student Class

The `Student` class represents an individual student and stores:

* Student ID
* Name
* Age
* Grade

Methods include:

* `display_details()`
* `get_details()`

### Course Class

The `Course` class represents an individual course and stores:

* Course Name
* Course Code
* Course Credits
* Enrolled Student IDs

Methods include:

* `display_course()`
* `get_info()`

### School Class

The `School` class manages the complete management system and provides operations such as:

* Loading records
* Saving records
* Adding students
* Adding courses
* Assigning courses
* Searching students
* Sorting records
* Updating student records
* Deleting student records
* Viewing students
* Viewing courses

## Example Record Lifecycle

```text
Add Student
    ↓
Add Course
    ↓
Assign Course
    ↓
Search Student
    ↓
Update Grade
    ↓
View Students
    ↓
Delete Student
```

This project demonstrates practical use of Object-Oriented Programming, file persistence, data validation, search operations, sorting algorithms, record management, and relationship mapping between students and courses within a real-world student management workflow.