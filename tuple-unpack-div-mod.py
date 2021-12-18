a = divmod(20, 8)
print(a)

t = (20, 8)
# print(divmod(*t)) # --> TypeError
print(divmod(*t))
print(*t)

