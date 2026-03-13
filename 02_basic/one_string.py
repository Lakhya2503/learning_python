
# -------------------- x --------------------

# String

fullName = "Laxman Shinde"
firstName = fullName[0:6] #when ur start from 0th index then u can use also *fullName[:6]
# print("print First Name :",firstName)
# ---- x ----
nameSlice = fullName[2:6] # start from 2nd and goes from 5 didn't include 6th index beacuse it's start from 2nd index
# print("print  :", nameSlice)
# ---- x ----
negativeNameSlice = fullName[-1:] # it's negative index -1 mean start from last counting
# print("print  :", negativeNameSlice)
# ---- x ----
numList = '0123456789'
# hoppingNumber = numList[0:7:2] # it is hope the 2 numbers like use start number 0,2,6
# print("print  :", hoppingNumber)
# ---- x ----
name = "  laxman shinde  "
stripName = name.strip()
# print("strip name : ",stripName)  #remove white space on starting and ending only didn't include under the letter white spaces
# ---- x ----
countesTheCharacter = "laxman shinde"
characterCount = countesTheCharacter.count("a") # you can use the word also for counting
print("where character a :", characterCount)
# ---- x ----
findCharcterOnIndex = "laxman shinde"
whereIsAcharcterInIndex = findCharcterOnIndex.find("a")
# print("where character a :", findAcharcterInIndex)
# ---- x ----
laptop = "lenovo"
qunatity = 2

stringOfWriting = "I ordered the {} {} laptop but i can't recived any...."
newString = stringOfWriting.format(qunatity, laptop)
# print(newString)

# -------------------- x --------------------
