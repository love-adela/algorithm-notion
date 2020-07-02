from itertools import combinations

lst = [param for param in range(5)]
k = 3

# bitmask
print('--------------------------------')
print('get combinations by bit shifting')
for elem in range(1 << len(lst)):
    if bin(elem).count('1') != k: continue
    
    for i in range(len(lst)):
        if (elem & (1<<i)) == 0:
            continue
        print(lst[i], end = ' ')
    print()

# combination
print('--------------------------------')
print('get combinations by itertools')
for c in combinations(lst, k):
    print(' '.join([str(x) for x in c]))
