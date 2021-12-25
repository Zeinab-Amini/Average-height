# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


#finding the sum of the numbers
total_height = 0
for height in student_heights:
    total_height += height

#finding the number of students 
#it will loop through untill doen so that is how we can add one
number_students = 0
for studnt in student_heights:
    number_students += 1


#finding the averge and rounding it
average_height = round(total_height / number_students)
print(average_height)