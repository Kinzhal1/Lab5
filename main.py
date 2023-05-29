a = [1, 2, 3, 7, 12, 15, 20, 200, 246, 356]
b = [4, 5, 71, 717, 7435, 8534, 9098, 10056, 11023, 12087]
c = []
for i in range(0,len(a)):
    c.append(a[i])
for x in range(0, len(b)):
    c.append(b[x])
c.sort()