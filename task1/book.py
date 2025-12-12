class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} written by {self.author}"

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
