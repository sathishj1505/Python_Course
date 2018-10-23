is_enabled = True
is_active = False

if is_enabled:
    print("Save button is enabled")
else:
    print("Save button is disabled")

if is_enabled and is_active:
    print("Both of the conditions are True")
elif is_enabled and not(is_active):
    print("Enabled but not Active")
if is_active or is_enabled:
    print("Any one condition is True")
#Comparisions
def max_fun(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
max_num = max_fun(3,7,12)
print(max_num)

#Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))
operator = input("Enter operator: ")

if operator == "+" :
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else :
    print("Invalid operator")


