
class Book:
    def __init__(self, isbn, title, author, category, price):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn
        self.price = float(price)
        self.sales = [0] * 12


    def get_category(self):
        return self.category

    def get_isbn(self):
        return self.isbn

    def set_sales(self, month, count):
        self.sales[month] = count

    def get_revenue(self, month):
        return self.price * self.sales[month]

    def get_year_revenue(self):
        return self.price * sum(self.sales)

    def to_string(self):
        return f"ISBN: {self.isbn} \nTitle and Author: {self.title}, {self.author} \nCategory: {self.category} \nPrice: R{self.price} \nSales: {self.sales}"



if __name__ == "__main__":
    pass
