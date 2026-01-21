from Product import Product
from ShoppingCart import ShoppingCart

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = ShoppingCart()
    
    def __repr__(self):
        return f"User({self.id}, {self.name})"

    def checkout_and_pay(self):
        if not self.cart.articles:
            print("No articles in the shopping cart")
            return .0
        total_price = self.cart.total_price()
        for product in self.cart.articles:
            product.buy(self.cart.articles[product])
        self.cart.clear()
        print(f"{self.name} has placed an order with a total value of €{total_price:.2f}.")
        return total_price 

if __name__ == "__main__":
    laptop = Product("001", "Laptop", 999.0, 5)
    anna = User("u001", "Anna")
    anna.cart.add(laptop,2)
    anna.cart.show()
    total_value = anna.checkout_and_pay()
    print(total_value)
    anna.cart.show()