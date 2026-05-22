# Write a Python program for printing the stars in a pattern using Nested for loop.

rowCount = int(input("Enter the number of rows: "))

for i in range(1, rowCount + 1):
    for j in range(i):
        print("*", end=" ")
    print()