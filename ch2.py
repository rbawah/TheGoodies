"""
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# - - - - - VS

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
##############
x = 'ABC'
codes = [ord(x) for x in x]
print(x)
print(codes)
###############
"""
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)