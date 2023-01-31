# Q4. Write a program to print the first non-repeated character from a string?

input_string = input("given string : ")
count = 0
for i in input_string:
    if input_string.count(i) == 1:
        print("first non repeated character : ", i)
        count = 1
        break

if count == 0:
    print("Every character is repeating in string")

    