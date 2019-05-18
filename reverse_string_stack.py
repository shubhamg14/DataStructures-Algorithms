from stack import Stack

def reverse_string(stack1,input_string):

    for i in range(len(input_string)):
        stack1.push(input_string[i])

    rev_str = ''
    while not stack1.is_empty():
        rev_str += stack1.pop()

    return rev_str

stack1 = Stack()
input_string='Hello'

print(reverse_string(stack1,input_string))