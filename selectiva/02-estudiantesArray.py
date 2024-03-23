students = [10, 20, 55, 76, 75, 100, 80, 90, 20, 20];

qualification1 = 0
qualification2 = 0
qualification3 = 0
qualification4 = 0

for student in students:
    if student >= 80 :
        qualification4 += 1
    elif student >= 70 and student <= 80: 
         qualification3 += 1
    elif student >= 50 and student <= 70 :
        qualification2 += 1
    elif student <= 50 :
        qualification1 += 1

print(f"{qualification4} obtuvieron una calificacion mayor a 80");
print(f"{qualification3} obtuvieron una calificacion mayor a 70 y menor 80");
print(f"{qualification2} obtuvieron una calificacion mayor a 50 y menor 70");
print(f"{qualification1} obtuvieron una calificacion menor a 50");
