import copy
# -------------------------- x --------------------------

# listOne = [1, 2, 3]
# listTwo = listOne

# it will change on both list (Array) beacuse he has hold a refrence *see the changes on ** listOne and listTwo
# listOne[0] = 55

# print("list one : ", listOne)
# print("list two : ", listTwo)

# -------------------------- x --------------------------

#  when u wan't to change only one you can use copy also ( scenario case )


# listOne = [1, 2, 3]
# listTwo = copy.copy(listOne)
## listTwo = listOne[:] # also u can use so he can create copy like slice start to end
## also use slice you wan't a deep list like ** [ 1,34,45,[2,4],45,52,[52,52]] like then use copy.deepcopy(listname)

# it will change on single list (Array) beacuse he has hold a copy *see the changes on ** listOne and listTwo
# listOne[0] = 55


# print("list one : ", listOne)
# print("list two : ", listTwo)

# -------------------------- x --------------------------

# when u explesitly value use
# Example like

# accountBalance = 2562.99
# print("account balance in round : ", int(accountBalance))


# accountBalance = 2562
# print("account balance in round : ", float(accountBalance))

# -------------------------- x --------------------------

# operator overloading
#  joint value befor he will decide the values are same data type

# firstName = "Laxman"
# lastName = " Shinde"

# print(firstName + lastName)


# error throw like
# name = "Laxman Shinde"
# age = 24

# throw the error beacuse this code will beacuse the user was age is number and name is string type but
# because trying to add two different data types.

# print(name + age)

# -------------------------- x --------------------------
