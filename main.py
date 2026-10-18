# STUDENT RECORD MANAGEMENT SYSTEM
# PROG211 - OBJECT-ORIENTED PROGRAMMING 1
# Education Domain - Digital Public Goods Principles


class Student:
    """Stores information about one student."""

    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_info(self):
        print("\nSTUDENT INFORMATION")
        print("------------------------------")
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("------------------------------")

    def update_course(self, new_course):
        self.course = new_course

    def get_student_id(self):
        return self.student_id

    def get_student_name(self):
        return self.name

    def get_student_course(self):
        return self.course


class StudentRegistry:
    """Manages student objects in a dictionary."""

    total_registered = 0

    def __init__(self):
        self.students = {}

    @staticmethod
    def validate_student_details(student_id, name, course):
        return bool(student_id.strip() and name.strip() and course.strip())

    def register_student(self, student):
        if student.student_id in self.students:
            print("This student ID already exists.")
            return False
        self.students[student.student_id] = student
        StudentRegistry.total_registered += 1
        print("Student registered successfully.")
        return True

    def display_students(self):
        if not self.students:
            print("No students registered yet.")
            return
        print("\nALL REGISTERED STUDENTS")
        print("==============================")
        for student in self.students.values():
            student.display_info()

    def search_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            student.display_info()
        else:
            print("Student not found.")

    def find_student(self, student_id):
        return self.students.get(student_id)

    def count_students(self):
        return len(self.students)

    @classmethod
    def get_total_registered(cls):
        return cls.total_registered

    def display_student_names(self):
        if not self.students:
            print("No student names to display.")
            return
        print("\nREGISTERED STUDENT NAMES")
        for student in self.students.values():
            print(student.student_id, "-", student.name)

    def display_students_by_course(self, course_name):
        matches = [s for s in self.students.values()
                   if s.course.lower() == course_name.lower()]
        if not matches:
            print("No students found for that course.")
            return
        for student in matches:
            student.display_info()


class Result:
    """Stores a student's subject, mark and grade."""

    def __init__(self, student_id, subject, mark, grade):
        self.student_id = student_id
        self.subject = subject
        self.mark = mark
        self.grade = grade

    def display_result(self):
        print("\nSTUDENT RESULT")
        print("------------------------------")
        print("Student ID:", self.student_id)
        print("Subject:", self.subject)
        print("Mark:", self.mark)
        print("Grade:", self.grade)
        print("------------------------------")

    def get_student_id(self):
        return self.student_id

    def get_subject(self):
        return self.subject

    def get_mark(self):
        return self.mark

    def get_grade(self):
        return self.grade


class ResultRegistry:
    """Stores and manages result objects in a list."""

    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)
        print("Student result saved successfully.")

    def display_all_results(self):
        if not self.results:
            print("No results have been recorded.")
            return
        print("\nALL STUDENT RESULTS")
        for result in self.results:
            result.display_result()

    def display_student_results(self, student_id):
        matches = [r for r in self.results if r.student_id == student_id]
        if not matches:
            print("No results found for this student.")
            return
        for result in matches:
            result.display_result()

    def display_results_by_grade(self, grade):
        self._display_matching_results(
            lambda r: r.grade.lower() == grade.lower(),
            "No results found for that grade."
        )

    def display_results_by_subject(self, subject):
        self._display_matching_results(
            lambda r: r.subject.lower() == subject.lower(),
            "No results found for that subject."
        )

    def _display_matching_results(self, condition, message):
        matches = [r for r in self.results if condition(r)]
        if not matches:
            print(message)
            return
        for result in matches:
            result.display_result()

    def count_results(self):
        return len(self.results)


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_mark():
    while True:
        try:
            mark = float(input("Enter the student's mark (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def display_main_menu():
    print("\n===================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("===================================")
    options = [
        "Register Student", "Display All Students", "Search for a Student",
        "Count Registered Students", "Display Student Names",
        "Display Students by Course", "Add Student Result",
        "Display All Results", "Display Results by Student ID",
        "Display Results by Grade", "Display Results by Subject",
        "Count Recorded Results", "Exit"
    ]
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")
    print("===================================")


def register_student_menu(registry):
    print("\nREGISTER A NEW STUDENT")
    student_id = get_non_empty_input("Enter Student ID: ")
    name = get_non_empty_input("Enter Student Name: ")
    course = get_non_empty_input("Enter Course: ")
    if not StudentRegistry.validate_student_details(student_id, name, course):
        print("Invalid student information.")
        return
    registry.register_student(Student(student_id, name, course))


def add_student_result_menu(registry, result_registry):
    print("\nADD STUDENT RESULT")
    student_id = get_non_empty_input("Enter Student ID: ")
    if registry.find_student(student_id) is None:
        print("Student ID does not exist. Register the student first.")
        return
    subject = get_non_empty_input("Enter Subject: ")
    mark = get_valid_mark()
    grade = get_non_empty_input("Enter Grade: ")
    result_registry.add_result(Result(student_id, subject, mark, grade))


def main():
    registry = StudentRegistry()
    result_registry = ResultRegistry()
    print("Welcome to the Student Record Management System.")
    print("Education Domain - Student Information Management")

    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student_menu(registry)
        elif choice == "2":
            registry.display_students()
        elif choice == "3":
            registry.search_student(get_non_empty_input("Enter Student ID to search: "))
        elif choice == "4":
            print("Total registered students:", registry.count_students())
        elif choice == "5":
            registry.display_student_names()
        elif choice == "6":
            registry.display_students_by_course(
                get_non_empty_input("Enter the course name: "))
        elif choice == "7":
            add_student_result_menu(registry, result_registry)
        elif choice == "8":
            result_registry.display_all_results()
        elif choice == "9":
            result_registry.display_student_results(
                get_non_empty_input("Enter Student ID: "))
        elif choice == "10":
            result_registry.display_results_by_grade(
                get_non_empty_input("Enter Grade to search: "))
        elif choice == "11":
            result_registry.display_results_by_subject(
                get_non_empty_input("Enter Subject: "))
        elif choice == "12":
            print("Total recorded results:", result_registry.count_results())
        elif choice == "13":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select 1 to 13.")


if __name__ == "__main__":
    main()
