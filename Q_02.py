# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. 
# You have to update the original array.

size = int(input("ENTER THE ARRAY SIZE : "))
lis = []
for i in range(size):
    element = int(input("ENTER THE ELEMENT TO BE ADDED : "))
    lis.append(element)
print("\ngiven array : ", lis)
print("Reveresed array : " ,lis[::-1])
