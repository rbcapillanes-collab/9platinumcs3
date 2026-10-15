class Publication:
    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author
        
    def get_title(self):
        return self.__title
    def set_title(self, title:str):
        self.__title = title

    def get_author(self):
        return self.__author
    def set_author(self, author:str):
        self.__author = author
        
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication):
    def __init__(self, number_of_pages:int):
        super().__init__("Unknown", "Unknown")
        self.number_of_pages = number_of_pages
    
    def get_number_of_pages(self):
        return self.number_of_pages
    
    def set_number_of_pages(self, number_of_pages:int):
        if number_of_pages < 0:
            print("Number of pages must be positieve.")
        else:
            self.number_of_pages = number_of_pages

class Magazine(Publication):
    def __init__(self, issue_number:int):
        super().__init__("Unknown", "Unknown")
        self.issue_number = issue_number
        
    def get_issue_number(self):
        return self.issue_number
    def set_issue_number(self, issue_number:int):
        self.issue_number = issue_number
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")

book1 = Book(310)
book1.set_title("The Hobbit")
book1.set_author("J.R.R. Tolkien")\
    
mag1 = Magazine(202)
mag1.set_title("National Geographic")
mag1.set_author("Various Authors")

print("Publication Information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310)
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}")

print("\nMagazine Information: ")
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number()}")
