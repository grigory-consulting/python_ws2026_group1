from Food import Food
from BioLabel import BioLabel

class BioFood(Food, BioLabel):
    def __init__(self, id, name, price , available, tag, tax, producer, expiry_date, label):
        Food.__init__(id, name, price, available, tag, tax, producer, expiry_date)
        BioLabel.__init__(label) 

print(BioFood.mro())