print('Таблица умноженя')
s = 10
for i in range(1, s+1):
     print(*range(i, i*s+1, i), sep='\t')
