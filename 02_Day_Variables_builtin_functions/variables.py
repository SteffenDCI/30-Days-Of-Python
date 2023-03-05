# Day 2: 30 Days of Python programming

import builtins
import math

first_name = 'Mister'
last_name = 'Python'
full_name = first_name + ' ' + last_name
country = 'Finland'
city = 'Helsinki'
age = 50
year = 2023
is_married = False
is_true = True
is_light_on = False
one, two, three, four = 1, 2, 3, 4


print(type(first_name))
print(len(first_name))
print(len(last_name))

if len(last_name) > len(first_name):
    print("Last name is longer that first name.")
elif len(last_name) < len(first_name):
    print("First name is longer than last name.")
else:
    print("First and last name have the same length.")
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Radius of a circle
radius = 30.0
area_of_circle = math.pi * (radius ** 2)
circumference_of_circle = math.pi * 2 * radius

print("Calculating the area of a circle: ")
radius_input = int(input("Enter the radius: "))
print(math.pi * radius_input ** 2)

first_name_user = input("Enter First Name: ")
last_name_user = input("Enter Last Name: ")
country_user = input("Enter your country: ")
age_user = int(input("Enter your age: "))


# Keywords

dir(builtins)
