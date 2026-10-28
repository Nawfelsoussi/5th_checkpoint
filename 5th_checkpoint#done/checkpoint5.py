# Instructions
#
# Create a numpy array called "grades" that contains the following grades:
# [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]
#
# 1. Import the numpy library and create the "grades" array as specified above.
# 2. Use numpy functions to calculate the mean, median, and standard deviation of the grades.
# 3. Use numpy function to find the maximum and minimum of the grades.
# 4. Use numpy function to sort the grades in ascending order.
# 5. Use numpy function to find the index of the highest grade in the array.
# 6. Use numpy function to count the number of students who scored above 90.
# 7. Use numpy function to calculate the percentage of students who scored above 90.
# 8. Use numpy function to calculate the percentage of students who scored below 75.
# 9. Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
# 10. Create a new array called "passing_grades" that contains all the grades above 75.
# 11. Print the result of all the above steps.
#
# Note:
# - To calculate percentage use numpy.mean(grades > 90) * 100
# - To extract the grades above 90 use grades[grades > 90]
# - To extract the grades above 75 use grades[grades > 75]
#
# You can use other numpy functions as well to analyze the data as you want.
# The above steps are just examples of what can be done.
import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print("mean:", np.mean(grades))
print("median:", np.median(grades))
print("standard deviation:", np.std(grades))
print("maximum:", np.max(grades))
print("minimum:", np.min(grades))
print("sorted grades:", np.sort(grades))
print("index of highest grade:", np.argmax(grades))
print("number of students above 90:", np.sum(grades > 90))
print("percentage above 90:", np.mean(grades > 90) * 100)
print("percentage below 75:", np.mean(grades < 75) * 100)
high = grades[grades > 90]
print("High performers:", high)

passing = grades[grades > 75]
print("Passing grades:", passing)