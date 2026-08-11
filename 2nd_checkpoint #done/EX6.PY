# Write a Python program to create a set.
# Write a Python program to iterate over sets.
# Write a Python program to add members in a set and to remove items from a given set.

a = {0, 1, 2, 3, 4}

print(f"You have this set: {a}")

adds = int(input("Add a positive number to the set: "))
rem = int(input("Remove a positive number from the set: "))

while adds <= 0 or rem <= 0:
    print("The numbers must be positive.")
    adds = int(input("Add a positive number to the set: "))
    rem = int(input("Remove a positive number from the set: "))

a.discard(rem)
a.add(adds)

print("\nElements of the set:")
for item in a:
    print(item)

print("\nSorted:")
print(sorted(a))
#DONE