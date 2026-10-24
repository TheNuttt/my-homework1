grades = [ 4, 5, 3, 5, 4, 2, 5 ]

minimum = grades[0] 
maximum = grades[0]
total = 0

for grade in grades:
    if grade < minimum:
        minimum = grade
    if grade > maximum:
        maximum = grade
total += grade

average = total / len(grades)            

print(f"Минимальная оценка: {minimum}")
print(f"Максимальная оценка: {maximum}")
print(f"Средний балл:  {average}")