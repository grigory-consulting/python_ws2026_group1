from Product import Product

class Electronics(Product):
    def __init__(self, id, name, price , available, tag, tax, producer, warranty):
        super().__init__(id, name, price, available, tag, tax )
        self.producer = producer
        self.warranty = warranty