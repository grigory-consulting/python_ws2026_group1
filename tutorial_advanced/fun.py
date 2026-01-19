

def cube(num): # one parameter
    return num**3 # one return value 

print(cube(4))

l = [cube(x) for x in range(100)]
print(l)


def add_three_numbers(a,b,c=1): # 3 parameters with one default argument c 
    print("a =", a, "b =", b, "c =", c)
    return a+b+c

#print(add_three_numbers(1))
print(add_three_numbers(1,2))
print(add_three_numbers(2,1))
print(add_three_numbers(1,2,3))
print(add_three_numbers(2,1))
print(add_three_numbers(c=4,b=2,a=10))
print(add_three_numbers(10,c=4,b=2))
# print(add_three_numbers(c=4,b=2,10)) # this is not allowed
# SyntaxError: positional argument follows keyword argument


# this is also not allowed
# SyntaxError: parameter without a default follows parameter with a default
# def add_three_numbers(a=1,b,c): 
#    print("a =", a, "b =", b, "c =", c)
#    return a+b+c

def my_print(*args): # number of parameters is arbitrary
    print("(", end = "")
    print(*args, sep = "|", end = "")
    print(")")

print(1,2,3,4,5,6, "number1", "number2")
my_print(1,2,3,4,5,6, "number1", "number2")

def manual_data_entry_tool(**kwargs):
    for key,value in kwargs.items():
        my_print(key,value)

manual_data_entry_tool(name = "Anna", city = "Berlin", age = "25")
manual_data_entry_tool(name = "Anna", city = "Berlin", age = "25", 
    street = "Unter den Linden")

def everything(a, b=1, *args, **kwargs): 
    print("a", a)
    print("b", b)
    print("args", args)
    print("kwargs", kwargs)

everything(1)
everything(1,2)
everything(1,2,3,4,5,6,"more args")
everything(1,2,3,4,5,6,name = "Anna", city = "Berlin", age = "25", 
    street = "Unter den Linden")
