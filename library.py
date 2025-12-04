# library management system
"""(register, login) -->user
(add book, issue book, return book, view book, search book)"""

# creating two file named users.txt and books.txt to store user
# information and books information permanently

import os
if not os.path.exists('users.txt'):
    with open('users.txt','w') as f:
        pass
import os
if not os.path.exists('books.txt'):
    with open('books.txt','w') as f:
        pass

# load data from the file
def load_user():
    """load all the users from user.txt into directory"""
    users_dict={}

    try:
        with open('users.txt','r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(',')
                    users_dict[username] = password
    except FileNotFoundError:
        print("file not found!")
    return users_dict

# book_id, title, auuthor, quantity
def load_books():
    books_list = []
    try:
        with open("books.txt",'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id,title,author,quantity = line.split()

                    book ={
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    books_list.append(book)
    
    except FileNotFoundError:
        print("file not found")
    return books_list

def get_existing_books_id(books_list):
    """create a set to store all the ids of the books"""
    books_ids = set()
    for books in books_list:
        # dictionary
        books_ids.add(book['id'])
    return books_ids

#user registration
def register_user(user_dict):
    """register a new user"""
    print("\n----------register a username--------------")
    username= input("enter the username:  ").strip()
    password= input("ehter the password:  ").strip()
    if username in user_dict:
        print(f"username already exists!")
        return False
    if not username or not password:
        print("username and password cannnot be empty")
        return False
    users_dict[username] = password
  
    # save the registered user to the file'users.txt'
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

    print("registration successful")
    return True

users_dict = load_user()
register_user(users_dict)

