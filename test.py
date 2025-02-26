

a = [2]
b = [1,2]

All_match = True
for x in a:
    if not x in b:
        All_match = False

if All_match == True:
    print('Yes!')
else:
    print('No')