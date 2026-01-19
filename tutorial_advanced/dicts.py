# Dictionaries

# mutable collection of key-value pairs
# keys are immutable, values are any type

d = {
    "one": 1,
    "two": [2],
    "three": "THREE",
    4: {"four": "FOUR"},
    (5,): [5.0, 5],
}

print(d)

# print(d["six"])

print(d.get("six", "No such key"))

# Delete 

del d["one"]

print(d)

val = d.pop(4) # delete and return

print(d)
print(val)

# iterate over the dictionary

for key in d:
    print(key, d[key]) # key, value

keys = list(d.keys()) # List of keys
values = list(d.values()) # List of values
items = list(d.items()) # List of key-value tuples

print(items)


# Exercise 1

colors = ["red", "red", "blue", "yellow", "blue", "brown", "brown", "blue"]

#import random

#with open("colors.txt", "a") as f: 
#    for _ in range(10000):
#        f.write(random.choice(colors) + "\n")



# TODO 
# Write a function that creates a dictionary, 
# that counts, how often each color occurs
# Result should be: d_color = {"red" = 2, "blue" = 3, ....}

#d_color = {} # empty dict
#d_color["color"] = 8 # you can assign new key:value-pairs
print("-----------Exercise 1-------------")

def count_colors(colors):
    d_color = {}
    for color in colors:
        if color not in d_color:
            d_color[color] = 1  # case when color not in dictionary
        else:
            d_color[color] += 1 # case when color in dictionary
    return d_color
def count_colors(colors):
    d_color = {}
    for color in colors:
        d_color[color] = d_color.get(color, 0) +1
    return d_color


d_color = count_colors(colors + colors + colors)
print(d_color)


from collections import Counter

print(Counter(colors))

# Exercise 2

languages = {"de": "german", "en": "english", "fra": "french"}
# Task: reverse the dictionary
# Result: {"german": "de", "english": "en", "french": "fra"} 

result = {}

for lang in languages:
    print(lang, languages[lang]) 
    result[languages[lang]] = lang

print(result)