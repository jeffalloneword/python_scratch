# from cloudacademy python course, updated for python 3
# modified 3/5/2023

my_name = "Patrick Bateman"
print("Hello and welcome " + my_name + "!")

quilt_width = 8
quilt_length = 8

print(quilt_width * quilt_length)

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 4)

my_team = (27 % 4)

print(my_team)

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)