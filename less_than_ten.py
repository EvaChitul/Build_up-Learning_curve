'''Take a list and write a program that prints out all the elements of the list that are less than 5. Instead of printing them one by one
make a new list that has all the elements less than 5 and print that list'''

list_to_use = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for i in list_to_use:
    if i < 5:
        print (i)
        new_list.append(i)
print (new_list)


