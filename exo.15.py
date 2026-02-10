#AIM: Demonstrate the use of a Python debugger (e.g., pdb or an IDE with debugging capabilities) on asample program with intentional errors.
#Guide students on setting breakpoints, stepping through code,and examining variable values.

print("UIN: 251P107 NAME: Aryan Devidas Khedekar")
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    avg = total / len(numbers)
    return avg
marks = [10, 20, 30, 40]
result = calculate_average(marks)
print("Average =", result)
                                
