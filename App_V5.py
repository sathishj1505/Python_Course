#Dictionaries
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
    #Key has to be unique
}
#access dictionary
print(month_conversions)
print(month_conversions["Mar"])
print(month_conversions.get("Jan"))
print(month_conversions.get("Apr", "Not a valid input"))

#While Loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Loop executed")

#Guessing Game
secret_word = "daredevil"
guess_word = ""
count = 0
guess_max = 5
guess_limit = False

while secret_word != guess_word and not(guess_limit):
    if count < guess_max:
        guess_word = input("Enter your guess: ")
        count += 1
    else:
        guess_limit = True

if guess_limit:
    print("You have reached guess limit")
else:
    print("You guessed the secret word!")

#For Loop
for letter in "Daredevil Season3":
    print(letter)
food_list = ["pizza","coke","biryani"]
for food in food_list:
    print(food)
for index in range(3, 10):
    print(index)
for index in range(len(food_list)):
    print(food_list[index])

