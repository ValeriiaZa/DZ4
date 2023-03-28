
x = int(input('Type number x:'))
y = int(input('Type number y:'))
o = input('choose operation(+,=,*,/):')
if o == '+':
    print (x + y)
elif o == '-':
    print(x - y)
elif o == '*':
    print(x * y)
elif o == '/' and y != 0:
    print(x / y)
else:print('Error')




