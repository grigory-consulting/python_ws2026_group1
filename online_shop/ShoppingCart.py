from Product import Product

class ShoppingCart:

    def __init__(self):
        self.articles = {}  #

    def __repr__(self):
        return f"ShoppingCart({self.articles})" 
    
    def add(self, product, quantity=1):
        # {"Product" : "quantity"}
        if quantity <= product.available:
            self.articles[product] = self.articles.get(product, 0) + quantity 
    
    def remove(self, product):
        del self.articles[product]
   
    def clear(self): # remove all items from shopping cart
        self.articles.clear()
    
    def total_price(self):
        total = 0
        for product in self.articles: # iterate over keys 
            total += product.price * self.articles[product]
        return total 
    
    def show(self):
        if not self.articles:
            print("Shopping Cart is empty!")
            return # the function evaluation ends here 
        print("Following articles are in the shopping cart:")
        for product in self.articles:
            quantity = self.articles[product]
            price_line = product.price * quantity
            print(f"    {product.name} x {quantity} = {price_line:.2f} €")
        print(f"Total price: {self.total_price():.2f} €")

if __name__ == "__main__":
    product1 = Product(id="001", name="MyBook", price= 20.99, available=5)
    product2 = Product(id="002", name="MyDVD", price= 19.99, available=20)
    sc = ShoppingCart()

    sc.add(product1)
    sc.add(product2,5)
    sc.show()
    #sc.clear()
    #sc.show()


    #product1.buy(sc[product1]) 
    #product2.buy(sc[product2])

    print(product1, product2)
    for product in sc.articles:
        product.buy(sc.articles[product])

    print(product1, product2)
else:
    print("loading ShoppingCart.py")