# 1. Write a python program to display a user entered name followed by Good Afternoon using
# input() function.
# name = input('Enter your name: ')
# print('Good Afternoon', name)

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# replaced_words = letter.replace('<|Name|>', 'Arsalan').replace('<|Date|>', '12/02/2089')
# print(replaced_words)

# 3. Write a program to detect double space in a string.
# linux = "Linux is a free, open-source  operating system"

# spaced = linux.find("  ")
# print(spaced)


# 4. Replace the double space from problem 3 with single spaces.
# linux = "Linux is a free, open-source  operating system"

# replaced = linux.replace("  ", " ")
# print(replaced)

# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n \tthis python course is nice. \nThanks!"
print(letter)