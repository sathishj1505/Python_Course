food_list = ["pizza","coke","biryani","chiken"]
#Access
print(food_list)
print(food_list[2])
print(food_list[2:])
print(food_list[1:3])
#Modify
food_list[1] = "fanta"
print(food_list[1])
num_list = [1,2,3,4,5,6,7,8,9]
#Functions
#Extend : append the list to add
food_list.extend(num_list)
print(food_list)
#Apeend : add at the end
food_list.append("coke")
print(food_list)
food_list.insert(2, "wine")
print(food_list)
#Remove
food_list.remove("chiken")
#Pop : removes the last element
food_list.pop()
#Search in list
food_list.index("biryani")
food_list.count("biryani")
#food_list.sort() asc oder
print(food_list)
#Delete everything
food_list.clear()

#Tuples
location = (4, 5, 7)
#tuple is immutable : cannot be modified
print(location[1])

