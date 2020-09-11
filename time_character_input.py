'''Create a program that asks the user to enter their name and their age.
Print a message addressed to them that tells them the year in which they will turn 100'''


name = input('What is your name? ')
age = int(input('What is your age? '))

import time

current_time = time.localtime()
current_year = current_time[0]
year_100 = current_year + (100-age)

print ('Hello ' + name + '!' + ' You will turn 100 in the year ' + str(year_100))
