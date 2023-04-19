# 7.Read a string and print the words in alphabetical order
str=input("Enter the string: ")
words=str.split(" ")
words.sort()
print("words in alphabetical order:",*words)