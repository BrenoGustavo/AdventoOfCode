a = [[0 for i in range(15)] for j in range(15)]
b = [[0 for i in range(15)] for j in range(15)]

a[0][0] = 1
a[0][1] = 2
a[0][2] = 3


print(len(a))
print(len(a[0]))

for i in a:
    print(''.join(str(i)))

for i in range(15):
    for j in range(15):
        # print(i, j)
        b[14 - i][14 - j] = a[i][j]

print('a ')
for i in b:
    print(''.join(str(i)))