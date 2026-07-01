# Python Student Management System

# Import search from regex and the type Self from typing
from typing import Self
from re import search

# Define Primary Constants for program
KEY = "pass12ssap21"  # Access code for admin view
STUDENT_HEADER: str = "STUDENT_ID || NAME || AGE || GRADE"
COURSE_HEADER: str = "COURSE_CODE || COURSE_NAME || COURSE_CREDITS"
FORMAT_TYPE_1: str = r"^\d+\s:\s[a-zA-Z\s]+\s:\s\d+\s:\s\d{1,2}[a-zA-Z0-9]$"
FORMAT_TYPE_2: str = r"^[a-zA-Z0-9\s]+\s\|\s[a-zA-Z\s]+\s\|\s\d+$"


class Course:
    """A Class that is used to model a modular course"""

    def __init__(self, course_name: str, course_code: str, course_credits: int) -> None:
        """Initializes the class with attributes course_name, course_code, course_credits and list of students"""
        self.course_name = course_name
        self.course_code = course_code
        self.course_credits = course_credits
        self.course_students: list[int] = []

    def display_course(self) -> str:
        """Method to display the primary course object details"""
        details: str = (
            f"{self.course_code} | {self.course_name} | {self.course_credits}"
        )
        return details

    @classmethod  # Decorator used to create a class, ie an alternative constructor
    def get_info(cls, record: str) -> Self:
        """Method to construct a course object from a string"""
        data: list[str] = record.split(" | ")
        return cls(
            course_code=data[0],
            course_name=data[1],
            course_credits=int(data[2]),
        )


class Student:
    """A Class that is used to model a Student"""

    def __init__(self, student_id: int, name: str, age: int, grade: str) -> None:
        """Initialize the class with student_id, name, age, and grade"""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self) -> str:
        """Method to display the primary student object details"""
        details: str = f"{self.student_id} : {self.name} : {self.age} : {self.grade}"
        return details

    @classmethod  # Decorator used to create a class, ie an alternative constructor
    def get_details(cls, record: str) -> Self:
        """Method to construct a course object from a string"""
        data: list[str] = record.split(" : ")
        return cls(
            student_id=int(data[0]),
            name=data[1],
            age=int(data[2]),
            grade=data[3],
        )


class School:
    """A Class used to model a school Object"""

    def __init__(self, name: str, file_location: str) -> None:
        """Initialized the class with name, file location, and a list for students and a list for courses"""
        self.name = name
        self.file_location = file_location
        self.students: list[Student] = []
        self.courses: list[Course] = []

    def load_records(self) -> None:
        """Method to load existing records from txt file"""
        try:
            # File open in read mode for accessing data
            with open(self.file_location, "r") as file:
                # Returns newline character as well with each line
                line: str
                for line in file:
                    # Conditions to identify record type
                    line = line.strip()
                    if line == COURSE_HEADER or line == STUDENT_HEADER:
                        continue
                    elif search(FORMAT_TYPE_1, line):
                        self.students.append(
                            Student.get_details(line)
                        )  # Uses Class for method call
                    elif search(FORMAT_TYPE_2, line):
                        self.courses.append(
                            Course.get_info(line)
                        )  # Uses Class for method call
                    elif line.isdigit():
                        self.courses[-1].course_students.append(
                            int(line)
                        )  # Index -1 to access last added course
                id_list: list[int] = []
                # Duplicate ID Check and Removal
                index: int
                for index in range(len(self.students)):
                    if self.students[index].student_id not in id_list:
                        id_list.append(self.students[index].student_id)
                    else:
                        self.students.pop(index)
        except FileNotFoundError:
            print(f"Sorry, the file {self.name} does not exist")

    def save_records(self) -> None:
        """Serializes current active collection properties safely out into external system files."""
        # File open in write mode for clearing current file and saving valid records
        with open(self.file_location, "w+") as file:
            file.write(f"{STUDENT_HEADER}\n")
            student_entries: list[str] = [
                f"{student.display_details()}\n" for student in self.students
            ]
            file.writelines(student_entries)  # Writes student entries
            file.write(f"\n{COURSE_HEADER}\n")
            course: Course
            for course in self.courses:
                file.write(f"{course.display_course()}\n")  # Writes course entries
                id: int
                for id in course.course_students:
                    file.write(f"{id}\n")  # Writes each student ID

    def add_student(self) -> None:
        """Method used to add a student object to students list"""
        for id in range(1, (len(self.students) + 2)):
            for student in self.students:
                new_id: bool = False  # Flag to check if the ID is unique
                if student.student_id != id:
                    new_id = True
                else:
                    break
            if new_id:  # condition to break loop on first unique ID found
                student_id: int = id
                break

        while True:
            name: str = input("Enter Student Name: ").title().strip()
            if len(name) < 1:
                print("Name cannot be empty")
            else:
                break
        while True:
            try:
                age: int = int(input("Enter Student Age: "))
            except ValueError:
                print("Error: Invalid input enter a valid age ")
            else:
                break
        while True:
            grade: str = input("Enter the grade of student: ").strip()
            if search(
                r"^\d{1,2}[a-zA-Z0-9]$", grade
            ):  # regex format check to validate grade
                break
            else:
                print(
                    "Error: Invalid format. Grade must be 1 or 2 digits followed by 1 Letter (e.g., 8B, 10A)."
                )

        student = Student(student_id, name, age, grade)
        self.students.append(student)
        print(f"Student {name} with ID {student_id} added succesfully")

    def add_course(self) -> None:
        """Method used to add a course object to courses list"""
        while True:
            course_name: str = input("Enter Course Name: ").strip().title()
            if len(course_name) < 1:
                print("Course Name cannot be empty")
            else:
                break
        while True:
            course_code: str = input("Enter Course Code: ").strip().upper()
            if len(course_code) < 1:
                print("Course Code cannot be empty")
            else:
                break
        while True:
            try:
                course_credits: int = int(input("Enter Course Credits: "))
            except ValueError:
                print("Error: Invalid input enter a valid number")
            else:
                if course_credits <= 40:
                    break
                else:
                    print("Maximum possible course credits is 40")
        course = Course(course_name, course_code, course_credits)
        self.courses.append(course)
        print(f" The Course {course_name} has been added succesfully")

    def search_student(self, modify_record: bool) -> int | None:
        """Method used to search for particular student record"""
        result_found: bool = False
        if not modify_record:  # Skips choice if record is to be deleted
            # Menu for search
            print("======= Search Menu =======")
            print("1. Student ID")
            print("2. Student Name")
            attribute_type: str = (
                input("Enter attribute to search (1 or 2): ").strip().lower()
            )
            while attribute_type not in [
                "1",
                "2",
            ]:  # Handles Invalid choice input
                print("\nInvalid choice entry")
                attribute_type: str = (
                    input("Enter your choice (1 or 2): ").lower().strip()
                )
        else:
            attribute_type: str = "1"

        if attribute_type == "1":
            while True:
                try:
                    student_id: int = int(input("Enter Student ID: "))
                except ValueError:
                    print("Error: Invalid input enter a valid ID number")
                else:
                    break
            if not modify_record:
                print("======= Search results =======\n")
            index: int
            for index in range(len(self.students)):
                if self.students[index].student_id == student_id:
                    result_found = True
                    if modify_record:
                        return index

                    else:
                        print(self.students[index].display_details())

        elif attribute_type == "2":
            student_name: str = input("Enter Student Name: ").title().strip()
            print("======= Search results =======\n")
            index: int
            for index in range(len(self.students)):
                if self.students[index].name.startswith(student_name):
                    result_found = True
                    print(self.students[index].display_details())
        if not result_found:
            print("No Student Record Found")

    def update_student(self) -> None:
        """Method used to update or modify existing student records"""
        print("======= Modify Records =======")
        print("1. Update Grade")
        print("2. Delete Student Record")
        choice: str = input("Enter your choice (1 or 2): ").lower().strip()
        while choice not in [
            "1",
            "2",
        ]:  # Handles Invalid choice input
            print("\nInvalid choice entry")
            choice = input("Enter your choice (1 or 2): ").lower().strip()
        index: int | None = self.search_student(True)
        # Condition to ensure search returned result
        if index is not None:
            if choice == "1":
                while True:
                    new_grade: str = input("Enter the grade of student: ").strip()
                    if search(
                        r"^\d{1,2}[a-zA-Z0-9]$", new_grade
                    ):  # regex format check to validate grade
                        break
                    else:
                        print(
                            "Error: Invalid format. Grade must be 1 or 2 digits followed by 1 Letter (e.g., 8B, 10A)."
                        )
                self.students[index].grade = new_grade
                print(
                    f"The grade of student {self.students[index].name} has been updated to {new_grade}"
                )
            elif choice == "2":
                # Course Student ID Removal when student record is deleted
                course: Course
                for course in self.courses:
                    id: int = self.students[index].student_id
                    while (
                        id in course.course_students
                    ):  # Loop to remove all instances of deleted ID
                        course.course_students.remove(id)
                # Perform pop operation after removing all ID instances
                removed_student: str = self.students[index].name
                self.students.pop(index)
                print(f"The student {removed_student} has been deleted")

    def sort_records(self) -> None:
        """Method used to sort the courses list and students list"""
        print("======= Choose Category =======")
        print("1. Students\n2. Courses")
        choice: str = input("Enter your choice (1 or 2): ").lower().strip()
        while choice not in [
            "1",
            "2",
        ]:  # Handles Invalid choice input
            print("\nInvalid choice entry")
            choice = input("Enter your choice (1 or 2): ").lower().strip()
        if choice == "1":
            print(
                "\nSort By \na. Student ID\nb. Student Name\nc. Student Age\nd. Student Grade"
            )
            option: str = input("Enter your choice (a, b, c or d): ").lower().strip()
            while option not in [
                "a",
                "b",
                "c",
                "d",
            ]:  # Handles Invalid choice input
                print("\nInvalid choice entry")
                option = input("Enter your choice (a, b, c or d): ").lower().strip()
            # Uses Lambda for instant function as key
            if option == "a":
                self.students.sort(key=lambda student: student.student_id)
            elif option == "b":
                self.students.sort(key=lambda student: student.name)
            elif option == "c":
                self.students.sort(key=lambda student: student.age)
            elif option == "d":
                self.students.sort(key=lambda student: student.grade)
        elif choice == "2":
            print("\nSort By \na. Course Code\nb. Course Name\nc. Course Credits")
            option: str = input("Enter your choice (a, b or c): ").lower().strip()
            while option not in [
                "a",
                "b",
                "c",
            ]:  # Handles Invalid choice input
                print("\nInvalid choice entry")
                option = input("Enter your choice (a, b or c): ").lower().strip()
            # Uses Lambda for instant function as key
            if option == "a":
                self.courses.sort(key=lambda course: course.course_code)
            elif option == "b":
                self.courses.sort(key=lambda course: course.course_name)
            elif option == "c":
                self.courses.sort(key=lambda course: course.course_credits)
        print("Records sorted successfully")

    def assign_course(self) -> None:
        """Method used to assign courses to student object by adding student within list in course object"""
        print("Choose Student and Course")
        index: int | None = self.search_student(True)
        # Condition to ensure search returned result
        course_added: bool = False
        if index is not None:
            course_name: str = input("Enter Course Name: ").title().strip()
            course: Course
            for course in self.courses:
                if course.course_name == course_name:
                    if self.students[index].student_id not in course.course_students:
                        course.course_students.append(self.students[index].student_id)
                        course_added = True
                    else:
                        print("Student already enrolled for aforementioned course")
            if not course_added:
                print("Such a course was not found")

    def view_students(self) -> None:
        """Method used to view the students list"""
        if self.students:
            student: Student
            for student in self.students:
                enrolled: bool = False
                print(student.display_details())
                print("Courses Enrolled In: \n")
                course: Course
                for course in self.courses:
                    if student.student_id in course.course_students:
                        print(f"{course.display_course()}")
                        enrolled = True
                if not enrolled:
                    print("No courses enrolled ")
                print("\n")
        else:
            print("No Students Records exist")

    def view_courses(self, admin_view: bool) -> None:
        """Method used to view the students list with possible view to students enrolled"""
        print(f"\n{COURSE_HEADER}")
        if self.courses:
            course: Course
            for course in self.courses:
                print(course.display_course())
                # Special passkey to grant access to students list by course
                if admin_view:
                    print(f"Students Present by ID: \n\t{course.course_students}\n")
        else:
            print("No Courses present")

    def management_interface(self) -> None:
        """Serves as the main loop processing CLI inputs continuously."""
        self.load_records()  # Bootstrap database parsing right away when the interface system begins running
        print(f"======= {self.name} Student Management System =======")
        while True:
            print(f"\n1. Add Student")
            print(f"2. Add Course")
            print(f"3. Assign Course")
            print(f"4. View Students")
            print(f"5. View Courses")
            print(f"6. Search Student")
            print(f"7. Sort Records")
            print(f"8. Update or Delete Record")
            print(f"\n\n Quit -q\n")

            choice: str = (
                (input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8 or q): "))
                .lower()
                .strip()
            )

            while choice not in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "q",
            ]:  # Handles Invalid choice input
                print("\nInvalid choice entry")
                choice = (
                    input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8 or q): ")
                    .lower()
                    .strip()
                )
            print("\n")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.assign_course()
            elif choice == "4":
                self.view_students()
            elif choice == "5":
                permission: str = input("Do you want to view is admin enter KEY: ")
                if permission == KEY:
                    self.view_courses(True)
                else:
                    self.view_courses(False)
            elif choice == "6":
                self.search_student(False)
            elif choice == "7":
                self.sort_records()
            elif choice == "8":
                self.update_student()
            elif choice == "q":
                self.save_records()
                break

            print(f"\nReturn to Menu -r\t\t Quit -q ")
            action: str = (input("Enter your choice (r/q): ")).lower().strip()
            while action not in ["r", "q"]:  # Handles Invalid choice input
                print("\nInvalid choice entry")
                action = input("Enter your choice (r/q): ").lower().strip()

            if action == "q":
                self.save_records()
                break


def main() -> None:
    # Initializes School Instance
    modern_school = School("Modern School", "file-manager/text-files/school.txt")
    modern_school.management_interface()


# Guard header in case imported
if __name__ == "__main__":
    main()
