# Q9. Write a program to reverse a stack.

# from collections import deque

class stack:
    def __init__(self):
        self.obj = []

    def push(self,element):
        self.obj.append(element)
        
    def pop(self):
        return self.obj.pop()

    def peek(self):
        return self.obj[-1]

    def is_empty(self):
        return len(self.obj) == 0

    def delete(self):
        self.obj.clear()

    def show(self):
        for value in reversed(self.obj):
            print(value)



def bottom_insertion(stack, element):

    if stack.is_empty():
        stack.push(element)

    else:
        temp = stack.pop()
        bottom_insertion(stack, element)
        stack.push(temp)

def reverse(stack):
    if stack.is_empty():
        pass
    else:
        temp = stack.pop()
        reverse(stack)
        bottom_insertion(stack, temp)

stk = stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Given Stack")
stk.show()
 
print("\nStack after Reversing")
reverse(stk)
stk.show()



