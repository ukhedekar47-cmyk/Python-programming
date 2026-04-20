# Odd even
num = int(input("Enter a number: ")) 
if num % 2 == 0: 
    print("Even number")
else: print("Odd number")


a = int(input("Enter first number: ")) 
b = int(input("Enter second number:")) 
c = int(input("Enter third number: ")) 
if a >= b and a >= c:
   print("Largest is:", a) 
elif b >= a and b >= c: print("Largest is:", b)
else: print("Largest is:", c)



#Student Result Calculator
marks = int(input("Enter marks: ")) 
if marks >= 90: print("Grade A") 
elif marks >= 75: print("Grade B") 
elif marks >= 50: print("Grade C") 
else:
 print("Fail")
 
  
#Sum of Digits
i = 1 
while i <= 10: 
    print(i) 
    i += 1
    
    
    n = int(input("Enter a number: ")) 
    i = 1; sum = 0
    while i <= n: 
        sum += i; i+= 1 
    print("Sum is:", sum)
    
    
    #Reverse Number Using While Loop
    num = int(input("Enter a number: ")) 
    reverse = 0 
    while num > 0: 
      digit = num % 10 
      reverse = reverse * 10 + digit; num = num // 10 
    print("Reversed number:", reverse)
    
    
    #Multiplication Table 
    num = int(input("Enter a number: ")) 
    for i in range(1, 11): 
        print(num,"x", i, "=", num * i)
        
        
        
#Count Vowels and Consonants        
string = input("Enter a string: ") 
count = 0 
for ch in string: 
            
 if ch.lower() in "aeiou": 
            count += 1 
            print("Number of vowels:", count)
            
            
            
#Factorial Using Recursion            
n = int(input("Enter a number: ")) 
fact = 1 
for i in range(1, n + 1): 
                fact*= i 
                print("Factorial is:", fact)
                
                
                


#Prime Checker
num = int(input("Enter a number: ")) 
flag = True 
if num <= 1: flag = False
else: 
                  for i in range(2, num): 
                   if num % i == 0: 
                    flag = False 
                    break 
if flag:
                   print("Prime number") 
else: 
    print("Not a prime number")
    
    
    
    
    
    
    
#Temperature Converter    
def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit =", celsius_to_fahrenheit(c))

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius =", fahrenheit_to_celsius(f))

    else:
        print("Invalid Choice")

# Electricity Bill Calculator (Slab Based)

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total Bill: ₹", bill)



