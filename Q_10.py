# Q10. Write a program to find the smallest number using a stack

inputs = int(input('length of stack : '))
stack = []
for n in range(inputs):
    numbers = int(input('Enter element: '))
    stack.append(numbers)
    
print("Smallest number in the stack is :  ", min(stack))