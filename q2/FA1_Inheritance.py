class Publication: # makes the Publication class
    def __init__(self, title:str, author:str): # makes the class properties and specifies what type of variables they are
        self.__title = title
        self.__author = author
        
    def get_title(self): # crceates the method, get_title, which will get the title name when called 
        return self.__title
    def set_title(self, title:str): # creates the method, set_title, which will change the title if used 
        self.__title = title

    def get_author(self): # creates the method, get_author, which will get the name of the author when called
        return self.__author
    def set_author(self, author:str): # creates the method, set_author, which will change the name of the author when used 
        self.__author = author
        
    def display_info(self): # creates method, display_info, in which when called it'll print the title of the book and its author 
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication): # creates the child class of the now superclass, Publication. Also creates its properties: number of pages and also the "Unknow, Unknown" represents how its as of now unknown since the superclass Publication doesnt have any inputs yet
    def __init__(self, number_of_pages:int):
        super().__init__("Unknown", "Unknown")
        self.number_of_pages = number_of_pages
    
    def get_number_of_pages(self): # creates the method, get_number_of_pages, and when called it'll get and display the number of pages of the book in publication
        return self.number_of_pages
    
    def set_number_of_pages(self, number_of_pages:int): # creates the method, set_number_of_pages, used when wanting to change the number of pages of the book in publicaion and also checks if its positive becausue a book cannot have negative pages
        if number_of_pages < 0:
            print("Number of pages must be positive.")
        else:
            self.number_of_pages = number_of_pages

class Magazine(Publication): # creates the class, Magazine, which is also a child class of Publication. Also creates its property issue number and again like the previous class it is "unknown, unknown" because they dont have any values yet and will only have values if the class above gets them
    def __init__(self, issue_number:int):
        super().__init__("Unknown", "Unknown")
        self.issue_number = issue_number
        
    def get_issue_number(self): # creates the method, get_issue_number, which will display the issue number when called 
        return self.issue_number
    def set_issue_number(self, issue_number:int): # creates the method, issue_number, which will be useful if you want to change the value of the issue number. 
        self.issue_number = issue_number
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #creates an object of the class Publication, in which the books name is "Journal of Experimental Psychology" and its authors being "Ratchiff, R. & Van Dongen, H."

book1 = Book(310) # it essentially "copies" what was in pub1 and changes it title and author by usig set_title and set_author. It also adds a new property to it, being number of pages in which here it is said to be 310.
book1.set_title("The Hobbit")
book1.set_author("J.R.R. Tolkien")
    
mag1 = Magazine(202) # it essentially "copies" what was in pub1 and changes it title and author by using set_title and set_author. It also adds a new property to it, being issue number in which here it is 202.
mag1.set_title("National Geographic")
mag1.set_author("Various Authors")

print("Publication Information: ") #shows the information of the title and author of the superclass, Publication since it is called in the following line. 
pub1.display_info() #title would be Journal of Experimenatl Psychology, and its authors would be Ratchiff, R. & Van Dongen, H. 

print("\nBook Information: ") # uses \n so that it can automatically have a space before it and sets the number of book pages in the class Book to -310 which it wont accept and show the error/warning message instead of setting the new page number of the negative quantity. Also displays info of the author anad title of the book
book1.set_number_of_pages(-310)
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}") #title would be The Hobbit, author being J.R.R Tolkien and number of pages would be 310. 

print("\nMagazine Information: ") # uses \m so that it can automatically have a space. Also shows the display info being the title and name of the authors and also shows the issue number of the magazine which would be 202. 
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number()}") #Title would be National Geography, authors woudl be Various Authors and issue number is 202
