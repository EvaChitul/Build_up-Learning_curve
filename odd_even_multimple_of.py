''' Ask for a number and let the user know if its odd or even. If the number is a multiple of 4 print a different message.
Ask the user for 2 numbers, and see if one is a multiple of the other
'''

numb = int(input ('Please give me a number:'))

if numb%4 == 0:
    print ('The number is a multiple of 4')
elif numb%2 == 0:
    print ('The number is even')
else:
    print ('The number is odd')