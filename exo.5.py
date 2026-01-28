print("UIN: 251P107,NAME: Aryan Khedekar")

       
task_list=[
    ("task 1","2025-02-26","High"),
    ("task 2","2025-02-07","Medium"),
   ("task 3","2025-02-08","Low"),
]

print("Intial Task List:")
print(task_list)

new_task=("Task 4","2025-02-09","High")
task_list.append(new_task)
print(task_list)

task_list.remove(task_list[1])
print(task_list)

task_list[1]=("Task 3","2025-02-08","High")
print(task_list)

task_list.sort()
print(task_list)

print("\nUpdated Task List:")
print(task_list)