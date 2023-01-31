# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

size = int(input("ENTER THE ARRAY SIZE : "))
lis = []
for i in range(size):
    element = int(input("ENTER THE ELEMENT TO BE ADDED : "))
    lis.append(element)
print("\ngiven list : ", lis)

given_number = int(input("ENTER YOUR NUMBER : "))
lis1 = []
for i in range(size):
    for j in range(i+1, size):
        if lis[i]+lis[j] == given_number:
            temp = (lis[i], lis[j])
            if temp not in lis1:
                lis1.append(temp)
print(lis1)













