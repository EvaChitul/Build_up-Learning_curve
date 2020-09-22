'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

number = int(input('Please insert a number: '))
divisor_list = []

for num in range(1, (int(number/2)+1)):
    if number % num == 0:
        divisor_list.append(num)

print('The divisors of ' + str(number) + ' are: ', divisor_list)