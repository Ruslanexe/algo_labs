w, h = map(int, input().split())
matrix = []
for i in range(h):
    matrix.append(input())

number = []
for i in range(h):
    number.append([])
    for j in range(w):
        number[i].append(0)

suma = dict()
symb = 'a'
while symb <= 'z':
    suma[symb] = 0
    symb = chr(ord(symb) + 1)

for i in range(h):
    number[i][0] = 1
    suma[matrix[i][0]] += 1

for col in range(1, w):
    tmp = dict()
    symb = 'a'
    while symb <= 'z':
        tmp[symb] = 0
        symb = chr(ord(symb) + 1)
    for row in range(h):
        c = matrix[row][col]
        number[row][col] = suma[matrix[row][col]]
        if matrix[row][col] != matrix[row][col-1]:
            number[row][col] += number[row][col-1]
        tmp[matrix[row][col]] += number[row][col]
    symb = 'a'
    while symb <= 'z':
        suma[symb] += tmp[symb]
        symb = chr(ord(symb) + 1)

if h == 1:
    print(number[0][w-1])
else:
    print(number[0][w-1] + number[h-1][w-1])
