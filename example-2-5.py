"""
To initialize tuples, arrays, and other types of sequences, you could also
start from a listcomp, but a genexp saves memory because it yields items
one by one using the iterator protocol instead of building a whole list just to
feed another constructor.
Genexps use the same syntax as listcomps, but are enclosed in parentheses
rather than brackets.
"""
symbols = '$¢£¥€¤'
tu = tuple(ord(symbol) for symbol in symbols)
print(tu)
#(36, 162, 163, 165, 8364, 164)

import array
ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)
#array('I', [36, 162, 163, 165, 8364, 164])