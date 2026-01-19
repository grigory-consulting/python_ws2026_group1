print("Hello World!")


# Comments: ignored by the interpreter
# line comment
my_string1 = "hello"
my_string2 = "WorlD"
my_string3 = "world" 
My_string3 = "world"

# Region comment (also docstring )
"""
my_string2 = "WorlD"
my_string3 = "world" 
My_string3 = "world"
"""

# string concatenation (merging)
print(my_string1 + " " + my_string2 + "!")

print(len(my_string2)) # number of characters of string = length 
print("The word " + "'"  + my_string2 + '"' +" has " + str(len(my_string2)) + " characters.")

# str -> type conversion 


a = "6"
b = "7"
print(a+b)

print(int(a) + int(b))


# Accessing the elements of string (character)

print(my_string1[0]) # first element
print(my_string1[1]) # second element
print(my_string1[-1]) # last element -> Python Feature
print(my_string1[-2]) # before last element 


# Case-sensitivity
print(my_string2)
print(my_string2.upper()) # everything is uppercase
print(my_string2.lower()) # everything is lowercase

print(my_string2.startswith("Wo")) # String starts with certain pattern 
print(my_string2.lower().startswith("wo")) # this is better
print(my_string2.endswith("Wo")) # String starts with certain pattern 


a = input("Enter a number:  ")
b = input("Enter a second number:  ")

# we get always strings from here
# convert strings to floats
product = float(a) * float(b)

print(f"The product of {a} and {b} is equal to {product}.")

