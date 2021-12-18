
# Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
#####

tshirt = (f'{c} {s}' for c in colors for s in sizes)
print(tshirt)

for t in tshirt:
    print(t)