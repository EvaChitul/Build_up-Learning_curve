list_one = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3]
list_two = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'c', 'f']

print (list_one.count(4))
list_one.pop(4)
print (list_one)

list_two.sort()
print (list_two)

from collections import deque

list_three = deque(list_two)
list_three.popleft()
print (list_three)

new_list = [i for i in range(20) if i%2 == 0]
print (new_list)

new_list_1 = [(x, y) for x in range (10) if x%3 == 0 for y in range (15) if y%5 == 0]
print(new_list_1)

vec_list = [-4, -3, -2, 0, 1, 2, 3, 4, 5]
vec_list_double = [x*2 for x in vec_list]
vec_list_poz = [x for x in vec_list_double if x >= 0]
print (vec_list_double)
print (vec_list_poz)

abc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_abc = [numb for elem in abc for numb in elem ]
print (new_abc)

matrix = [
    [1 , 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
new_matrix = [[line[i] for line in matrix] for i in range (5)]
print (new_matrix)

reverse_matrix = [[elem[i] for elem in new_matrix] for i in range(3)]
print (reverse_matrix)

if (matrix == reverse_matrix):
    print (True)

second_matrix= []
for i in range (5):
    second_matrix.append([elem[i] for elem in matrix])

print (second_matrix)
print ([e for sublist in matrix for e in sublist])