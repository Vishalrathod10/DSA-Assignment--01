# Q8. Write a program to check if all the brackets are closed in a given code snippet.


def is_balanced(expression):
    stack = []
    for i in expression:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if not stack:
                return False

            curr_char = stack.pop()
            if curr_char == '(':
                if i != ')':
                    return False

            if curr_char == '[':
                if i != ']':
                    return False

            if curr_char == '{':
                if i != '}':
                    return False

    if stack:
        return False
    else:
        return True

expression = "({()})()()"
balance = is_balanced(expression)
print(balance)
