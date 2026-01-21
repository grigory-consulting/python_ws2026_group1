from Product import Product
from datetime import date # class for date / datetime

class Food(Product):

    def __init__(self, id, name, price , available, tag, tax, producer, expiry_date ):
        super().__init__(id, name, price, available, tag, tax = 0.07)
        self.producer = producer 
        self.expiry_date = expiry_date


# 21.01.2026
# dd.mm.YYYY
# 2026/01/21
# 01-21-2026
# Jan 21 2026 