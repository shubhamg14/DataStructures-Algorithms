from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_parenthesis_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        parenthesis = paren_string[index]
        if parenthesis in '({[':
            s.push(parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top_element = s.pop()
                if not is_match(top_element, parenthesis):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print (is_parenthesis_balanced('{()}'))

