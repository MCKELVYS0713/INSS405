number = int(input('Enter a number:'))
if number % 15 ==0:
    print('Bowie State University')
elif number % 5==0:
    print('Bowie State')
elif number % 3==0:
    print('Bowie')
else:
    print('The number is not divisible by 3, 5, or 15.')