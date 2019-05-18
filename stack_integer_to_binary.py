from stack import Stack

def divide_by_two(number):
    s = Stack()

    while number > 0:
        remainder = number%2
        s.push(remainder)
        number = number//2

    binary_number = ''
    while not s.is_empty():
            binary_number += str(s.pop())

    return binary_number

print(divide_by_two(341))