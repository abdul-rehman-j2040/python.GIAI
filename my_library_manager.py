import streamlit as st
import json
import os

# setting a file of .json to store the data of books
file = "library.json"

# 1.load & 2.save library data
def load_library_books():
    if os.path.exists(file):
        try:
            with open("library.json","r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    else:
        return [] 
books = load_library_books

def save_library(books):
    with open (file,"w") as file:
        json.dump(books,file,indent=4)

#extracting Name_Of_Books
def N_O_B():
    booksnames=[]
    for book in books:
        booksnames.append(book["title"])
    return booksnames

# Giving Title Output To User for UI
st.title("Personal Library Manager")
main = st.sidebar.radio(" **Select an option** ",["Add New Book", "Show Library Books","Delet Book", "Save and Exit"])

# Making Input Form to take multiple inputs from user

# 1.Adding New Books function
def add_new_book():
    with st.form("add_book_form"):
        book_title = st.text_input("Book Name",placeholder="Enter the Book Name")
        book_author = st.text_input("Author Name",placeholder="Enter the Book's Author Name")
        publication_year = st.text_input("Year Of publish",placeholder="Enter the Book's published year")
        book_quantity = st.number_input("Book Quantity", min_value=1,placeholder="Enter the Book Quantity", value=10)
        book_genre = st.text_input("Book Genre", placeholder="Enter the Book Genre")
        book_price = st.number_input("Book Price", min_value=0,placeholder="Enter the Book price", value=1500)
        is_read = st.checkbox("Have you read this book?")

        newBook = {
            "title":book_title,
            "author":book_author,
            "genre":book_genre,
            "price":book_price,
            "qnty":book_quantity,
            "publish_year":publication_year,
            "isRead":is_read
        }
         
        if st.form_submit_button("Add New Book"):
            books.append(newBook)
            save_library(books)

# 2.Remove Books function
def Delet_book():
    st.subheader("Delet Book 🗑")
    book_name = st.selectbox("Enter the Book Name that you want to delet")
    if st.button("Remove Book"):
        updateBook = [book for book in books if book["title"] != book_name]
        st.info("Book has Been Deleted Sovvessfully..!")
        save_library(updateBook)
if main == "Show Library Books":
    show_books()
if main == "Add New Book":
    add_new_book()