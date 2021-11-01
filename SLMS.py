'''
We want to create a simple library management system. Lets call it LMS

Key things things we want to handle:
Borrowing
Returning
Inventory
A person should be able to borrow a book and the inventory should reflect this. Same applies to returning.For inventory, Ideally we want to have a title of the book and the count. The library manager should be able to add more books to the inventory
Extra
We can track who is borrowing books using their ID number. So we should be able to know who has what books.
'''
books = ['book1', 'book2','book3','book4','book5']
book_count = [3,2,4,2,1]
def main():
    print("Welcome to the Library Management System")
    menu = input("Choose your appropriate operation\n"
                 "[1] Borrow\n"
                 "[2] Return\n"
                 "[3] Check Inventory\n"
                 "[4] Exit\n")
    if menu == 1:
        pass
    if menu == 2:
        pass
    if menu == 3:
        pass
    if menu == 4:
        exit()

def borrow():

