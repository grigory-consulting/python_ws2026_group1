

x = (1,2,3)

# but immutable

# x[0] = 99: TypeError

# shallow immutability, so be careful

l1 = ["a", "b", "c"]
x = (l1,) # put the list into the tuple

print(x)

l1[0] = "D"

print(x)

