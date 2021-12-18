# Tuples used as records

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
print('======')
for passport in traveler_ids:
    print('%s --> %s' % passport)
