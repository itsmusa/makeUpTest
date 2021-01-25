from book import Book

def insertion_sort(books):
    for i in range(1, len(books)):
        while books[i-1].get_year_revenue() > books[i].get_year_revenue() and i > 0:
            books[i], books[i-1] = books[i-1], books[i]
            i = i - 1
    return books


def most_revenue(books, month):
    most_sales = books[0]
    for book in books:
        if book.get_revenue(month) > most_sales.get_revenue(month):
            most_sales = book
    return most_sales


def get_revenue_category(books, category):
    category_revenue = 0
    for book in books:
        if book.get_category() == category:
            category_revenue = category_revenue + book.get_year_revenue()
    return category_revenue


def books_array(file_name):
    books = []
    with open(file_name, 'r') as bf:
        bf.readline()
        for line in bf:
            book_info = line.split(',')
            book_object = Book(book_info[0], book_info[1], book_info[2], book_info[3].strip(), book_info[4].strip(' \n'))
            books.append(book_object)
    return books


def set_book_sales(file_name, books):
    with open(file_name, 'r') as sf:
        for line in sf:
            book_isbn = line.split(', ')[0]
            book_copies_sold = line.split(', ')[1].split()
            for book in books:
                if book.get_isbn() == book_isbn:
                    for i in range(len(book_copies_sold)):
                        book.set_sales(i, int(book_copies_sold[i]))



def display_books(books):
    books = insertion_sort(books)
    for book in books:
        print(book.to_string())
        print()


def main():
    books = books_array('books.txt')
    set_book_sales('sales.txt', books)
    display_books(books)
    print()
    print(f"MOST REVENUE IN JULY:\n{most_revenue(books, 6).to_string()}")
    print()
    print(f"REVENUE BY BIOGRAPHIES\nR{get_revenue_category(books, 'biography')}")


if __name__ == "__main__":
    main()
