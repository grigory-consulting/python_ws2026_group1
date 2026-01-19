

for i in range(10):
    print(i, end=" ")
print()

for var in range(2,6):
    y = var*var
    print(var, y, end=" | ")
    print(f"The square of {var} is {y}.")

l1 = [1, 2, 3]
l2 = [1.0, 2, "3"] # float, int, string
print(l2)
l3 = [1., 2, "3", l2] # list that contains list
print(l3)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for each in fruits: # for each-like loops
    print(each)

# List comprehension

numbers = list(range(1,101))

print(numbers)

cubes = [i**3 for i in numbers] # much better

# without list comprehension

cubes = []
for i in numbers:
    cubes.append(i**3)

# the bad way
cubes = []
for i in numbers:
    cubes += [i**3] # list concatencation (do not do it)

print(cubes)


food = ["rice", "beans", "bread"]

food.append("broccoli") 
print(food)

food += ["pizza", "hotdog"] # concatenation 

# slices
print(food[0]) # first element
print(food[:1]) # last element
print(food[2:]) # from third to end
print(food[:2]) # from start to second 
print(food[2:5]) # from third to fifth 
print(food[5:2:-1]) # start, end, stop 
print(food)

## Exercise 1 

words = ["apple", "egg", "banana", "sky", "time"]

a = 5 + 3 + 6 + 3 + 4 
print(a/5)

# Calculate the average word length 
total = 0
for word in words:
    total += len(word)
average = total / len(words)
print(average)


names = ["Anna", "Ben", "Alex", "Marie", "Andreas", "Lena"]

# Filter the list names, such that only names that start with the letter "A" appear
names_w_A =[] 
for name in names:
    if name.lower().startswith("a"):
        names_w_A.append(name)

print(names_w_A)

names_w_A = [name.upper() for name in names if name.lower().startswith("a")]

print(names_w_A)


#print()

l1 = [1,2,2,2,3,4,4,5,6,7,7,8,8,9,1,3,4,5,6,7,8,8,8,8,8,8]

# Remove the duplicates 
# Result: l2 = [1,2,3,4,5,6,7,9]

l2 = []
for elem in l1:
    if not (elem in l2): # elem in l2 -> membership check
        l2.append(elem)

print(l2)

l1 = [1,2,2,2,3,4,4,5,6,7,7,8,8,9,1,3,4,5,6,7,8,8,8,8,8,8]

l2 = []
for elem in l1:
    if elem in l2: # elem in l2 -> membership check
        print(elem, "Skipped")
        continue # skip the iteration 
    print(elem, "Appended")
    l2.append(elem)



print(l3)




# TODO we will visit here again 

l3 = [3,6,7,5,3,5,8,2,1,9,4]

# Find all pairs so that their sum is equal to 10
# Solution:
# [[3,7], [5,5], [8,2], [1,9], [6,4]]

res = []
for i in l3:
    for j in l3:
        if i+j == 10:
            if i<=j:
                if [i,j] not in res:
                    res.append([i,j])

print(res)

res = []
for i in l3:
    for j in l3:
        if i+j == 10 and i<=j and [i,j] not in res:
            res.append([i,j])

print(res)


print()