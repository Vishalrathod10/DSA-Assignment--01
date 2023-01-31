# Q3. Write a program to check if two strings are a rotation of each other?


str1 = input("first str : ")
str2 = input("second str : ")
if len(str1) == len(str2) :
    temp = str1 + str1
    if str2 in temp:
        print("given strings are rotation of each other")
    else:
        print("given strings are not rotation of each other")

else:
    print("given strings are not rotation of each other")