day_hours = 24
week_days = 7
print(day_hours * week_days)

student_grades = [9.1, 8.8, 7.5]
# List Slicing
print(student_grades[:2]) # Prints from the 0th index to the 2 index
print(student_grades[-1]) # Prints the last index (7.5)
print(student_grades[:-2]) # Prints the last two items in the array (tail)


# print(list(range(69,420)))

# def calculate_length(lst):
#   return len(lst)
    

# List Comprehension
temps = [221, 222, 256, 290]    
new_temps = [temp / 10 for temp in temps] # THIS LINE
print (new_temps)

temps = [221, 222, 256, 290, -9999]    
new_temps = [temp / 10 for temp in temps if temp != -9999] # THIS LINE
print (new_temps)

# def funkyfunc(functhat):
#     zzz = [sweetbabyjesus / 10 for sweetbabyjesus in functhat if isinstance(sweetbabyjesus, int)] # If this had an else, i'd need to move the if/else before the for x in xs
#     return zzz


# def funkyfunc(functhat):
#     zzz = [sweetbabyjesus if isinstance(sweetbabyjesus, int) and sweetbabyjesus > 0 else 0 for sweetbabyjesus in functhat] # If this had an else, i'd need to move the if/else before the for x in xs
#     return zzz

def funkyfunc(functhat):
    output = 0
    for dcmals in functhat
        output = float(output) + output
    return ouput

print(funkyfunc([99, 'no data,', 55]))