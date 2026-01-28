print("UIN: 251P107,NAME: Aryan Khedekar")

print("Choose a geometric figure to calculate it's area: ")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = input("Enter 1, 2 or 3: ")

if choice =="1":
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.141159
    area = pi*radius*radius
    print("The area of the circle is: ", area)
    
elif choice == "2":
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of the rectnagle: "))
    area = length*width
    print("The area of the rectangle is: ", area)
    
elif choice == "3":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of thetriangle: "))
    area = 0.5*base*height
    print("The area of the triangle is: ", area)
            
    
