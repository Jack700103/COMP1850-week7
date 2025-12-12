"""
Student class implementation for COMP1850 Worksheet 1.7, Task 1.1.
This module defines a Student class with basic student information and display functionality.
"""

class Student:
    """A class representing a student with name and student ID."""
    
    def __init__(self, name, student_id):
        """
        Initialize a Student object with name and student ID.
        
        Args:
            name (str): The student's name
            student_id (str): The student's unique identifier
        """
        self.name = name
        self.student_id = student_id
    
    def print_details(self):
        """
        Print the details of the student in a formatted way.
        
        Outputs:
            Prints student name and ID to the console
        """
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
    
    def __str__(self):
        """
        Return a string representation of the student.
        
        Returns:
            str: A formatted string containing student information
        """
        return f"Student: {self.name} (ID: {self.student_id})"


def main():
    """
    Main function to demonstrate the Student class functionality.
    Creates multiple student objects and calls their print_details methods.
    """
    student1 = Student("John Doe", "S12345")
    student2 = Student("Jane Smith", "S67890")
    student3 = Student("Alex Johnson", "S24680")

    print("=" * 40)
    print("STUDENT INFORMATION")
    print("=" * 40)
    
    print("\nStudent 1:")
    student1.print_details()
    
    print("\n" + "-" * 40)
    print("Student 2:")
    student2.print_details()
    
    print("\n" + "-" * 40)
    print("Student 3:")
    student3.print_details()
    
    print("\n" + "=" * 40)
    print("USING __str__ METHOD")
    print("=" * 40)

    print(f"\nString representation of student1: {student1}")
    print(f"String representation of student2: {student2}")
    print(f"String representation of student3: {student3}")


if __name__ == "__main__":
    main()