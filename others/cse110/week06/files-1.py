with open('week06/books.txt') as books_file:
    for book_name in books_file:
        book_name = book_name.strip()
        print(book_name)