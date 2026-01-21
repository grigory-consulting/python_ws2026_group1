from Product import Product

class Book(Product):

    def __init__(self, id, name, price , available, tag, tax = 0.07, author = "", isbn = ""):
        super().__init__(id, name, price, available, tag, tax )
        self.isbn = isbn
        self.author = author 

# TODO in new scripts: class Food, class Electronics 

