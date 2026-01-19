

class Product:
    def __init__(self, id, name = "", price = 1.0 , available = 0,
     tag = "", tax = 0.19):
        self.id = id
        self.name = name
        self.price = price
        self.available = available
        self.tag = tag
        self.tax = tax
    
    def __str__(self):
        # TODO -> print brutto and netto
        return f"{self.name} | {self.price:.2f} € | Quantity available: {self.available}"
    
    def __repr__(self):
        return f"Product({self.id},{self.name},{self.price},{self.available},{self.tag},{self.tax})"
    
    def buy(self, quantity):
        if self.available >= quantity:
            self.available -= quantity 
        else:
            print("Not enough in the stock") # TODO later we will built in an error
    
if __name__ == "__main__": # check whether entry point is at current script 
    p1 = Product("0.01", "product", 20.99, 5)
    print(p1)
    print([p1])
    p1.buy(5)
    print(p1)
    p1.buy(1)
else:
    print("loading Product.py...")