
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b) # True
print(b)

b[-1].append(99) # Last element in b is mutable (list)
print(a == b)# False
print(b)