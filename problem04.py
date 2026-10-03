# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# dic = {
#     'naam': 'name',
#     'kaam': 'work',
#     'hath': 'hand',
#     'aakhir': 'end'
# }
# print(dic)


# 2. Write a program to input eight numbers from the user and display all the unique numbers
# (once).
# s = {
#     int(input("Enter number 1: ")),
#     int(input("Enter number 2: ")),
#     int(input("Enter number 3: ")),
#     int(input("Enter number 4: ")),
#     int(input("Enter number 5: ")),
#     int(input("Enter number 6: ")),
#     int(input("Enter number 7: ")),
#     int(input("Enter number 8: "))
# }
# print(s)


# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# se = {18,'18'}
# print(se)


# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# print(len(s))


# 5.
# s = {}
# What is the type of 's'?

# s = {}
# print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
# fav_lan = {}

# for i in range(4):
#     name = input("Enter your name: ")
#     lang = input("Enter your favourite programming language: ")

#     fav_lan[name] = lang

# print(fav_lan)


# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# When a duplicate key (name) is entered, the previous friend's language will be overwritten, and only the updated value will remain in the dictionary.



# 8. If languages of two friends are same; what will happen to the program in problem 6?
# Nothing will break—the program will execute normally and store all 4 entries because Python dictionaries allow duplicate values, requiring only the keys (names) to be unique.



# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# The Answer is NO