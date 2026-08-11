#Write a Python program to get a list, sorted in increasing order by the last element in each tuple,
#  from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#Hint: You can use the sort function.

numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def num(item):
    return item[1]

numbers.sort(key=num)

print(numbers)
#done