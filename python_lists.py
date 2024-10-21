#Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#Sort the grades in descending order and print the sorted list.

grades.sort(reverse= True)

print(grades)

# Task 2: Calculate the average grade and display it.

average = int(sum(grades) / len(grades))

print(average)
