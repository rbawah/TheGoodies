def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2)) 
tm = (10, 'alpha', [1, 2]) # Contains mutable element

print(fixed(tf)) # - -> True
print(fixed(tm)) # - -> False

