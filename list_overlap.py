'''
Take two lists and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

first_list = list(range(20))
second_list = [x**2 for x in range(20)]

print(first_list)
print(second_list)

common_list = [elem for elem in first_list if elem in second_list]
print(common_list)