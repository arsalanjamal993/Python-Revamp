# 1. Write a program to store seven fruits in a list entered by the user.
# fruits = []

# for i in range(7):
#     fruit_name = input("Enter fruit name here: ")
#     fruits.append(fruit_name)

# print(fruits)
# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
# marks = []

# for i in range(6):
#     subjects = int(input("Enter your subjects marks: "))
#     marks.append(subjects)

# marks.sort()
# print(marks)


# 3. Check that a tuple type cannot be changed in python.
# a = (1,2,3,4,5)

# a[0] = 10
# print(type(a))


# 4. Write a program to sum a list with 4 numbers.
# num = [1,2,3,4]

# print(sum(num))

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

counted = a.count(0)
print(counted)