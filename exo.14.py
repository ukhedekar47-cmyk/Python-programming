print("UIN: 251P107,NAME: Aryan Khedekar")

try:
    a = int(input('Enter a number: '))
    b = 10/a
    print(b)
    
except ZeroDivisionError:
    print('Divivsion by zero error')

except ValueError:
    print('Invalid input')
    
            