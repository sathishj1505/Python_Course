#Hello Jana
print("Hello Jana")
#Variables
character_name = "Jana"     #String
character_age: int = 25     #Numbers
is_Male = True              #Boolean
print("My name is " + character_name + ",")
print("My age is ",character_age,".")
#Strings
statement = "Matt Mudrock is DareDevil"
print(len(statement))
print(statement[3])
print(statement.index("t"))
print(statement.index("Mud"))
print(statement.replace("tt","ja"))
#Numbers
print(10 % 3) #10 mod 3 gives Reminder
test_num_1 = -77
test_num_2 = 3
print(abs(test_num_1))
print(pow(3, test_num_2))
print(max(4, 77))
#Importing a library
from math import *
print(floor(4.65))
print(ceil(4.65))
print(sqrt(test_num_2))
#Get input from user
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello : " +user_name+ "!")
print("You are ",user_age)
#Calculator
num_1 = input("Enter your number: ")
num_2 = input("Enter your number: ")
result_1 = int(num_1) + int(num_2)
#int function is looking for whole numbers
num_3 = input("Enter your number:")
result_2 = float(result_1) + float(num_3)
print(result_1)
print(result_2)
#Mad Lib Game
new_join = input("Enter the new joiner name")
company = input("Enter the company name")
team = input("Enter the team name")
role = input("Enter the role")
print("Welcome abroad " +new_join)
print("We " +company+ " would like to join you in " +team)
print("You will be working as " +role)




