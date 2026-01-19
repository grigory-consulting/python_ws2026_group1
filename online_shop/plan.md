# Plan - Online Shop

- class Product 
    - attributes
        - id 
        - name
        - price
        - available (quantity)
        - tag
        - tax
    - methods 
        - __str__, __repr__
        - buy
- class ShoppingCart
    - attributes
        - articles = dict({Product:quantity}) of objects of class Product 
    - methods 
        - add
        - remove
        - clear ... remove all
        - calculate total price
        - show ... show everything what is in
- class User
    - attributes
        - id
        - name ... all metadata 
        - ShoppingCart 
    - methods 
        - pay 
        - checkout 


- class Ad 