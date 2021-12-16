# List Comprehension - Cartesian Products
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)
#######
for color in colors:
    for size in sizes:
        print((color, size))