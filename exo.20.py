# AIM: Develop a Python GUI application that performs various unit conversions such as currency  
# (Rupees to Dollars), temperature (Celsius to Fahrenheit), and length (Inches to Feet). The application should includefrom dataclasses import fields
# input fields for the values, dropdown menus or buttons to select the type of conversion, and labels to display the results.
print("UIN: 251P107, NAME: Aryan Khedekar")

import tkinter as tk    

def btnHandler():
    try:
        value = float(inputValue.get())
        choice = option.get()
        if choice == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            output.config(text="Result: " + str(result) + "°f")
        elif choice == "Rupees to Dollars":
            result = value / 83
            output.config(text="Result: " + str(result) + " $" + str(round(result,2)))
        elif choice == "Inches to Feet":
            result = value / 12
            output.config(text="Result: " + str(result) + " ft")
            
    except:
        output.config(text="Enter valid number")
        
root = tk.Tk()
root.title("Unit Converter Application")
root.geometry("350x300")

tk.Label(root, text="Unit Converter Application").pack(pady=10)
tk.Label(root, text="Enter value: ").pack()
inputValue = tk.Entry(root)
inputValue.pack(pady=5)

option = tk.StringVar()
option.set("Celsius to Fahrenheit")
menu = tk.OptionMenu(root, option, "Celsius to Fahrenheit", "Rupees to Dollars", "Inches to Feet")
menu.pack(pady=10)

tk.Button(root, text="Convert", command=btnHandler).pack(pady=10)
output = tk.Label(root, text="Result will appear here")
output.pack(pady=10)

root.mainloop()

     
                    
            