class Student:
    """
    Represents a student with unique ID, name and email.

    Attributes:
        id (str): Student identification number
        name (str): Full name of the student
        email (str): Institutional email address
    """
    
    def __init__(self, id, name, email):
        """
        Initialize Student instance with provided details.
        
        Args:
            id (str): Student ID
            name (str): Student name
            email (str): Contact email
        """
        self.id = id
        self.name = name
        self.email = email

    def print_details(self):
        """
        Generate formatted string containing student details.
        
        Returns:
            str: Formatted details in 'ID: [id], Name: [name], Email: [email]' format
        """
        return f'Id: {self.id}, Name: {self.name}, Email: {self.email}'

student_1 = Student("xnct0258","John Smith", "johnsmith@leeds.ac.uk")
print(student_1.print_details())  

student_2 = Student("jytbuwqr","Varia Costantine", "v.constantine@leeds.ac.uk")
print(student_2.print_details())
