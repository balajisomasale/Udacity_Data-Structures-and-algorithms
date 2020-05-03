# In this exercise you are going to apply what you learned about stacks with a real world problem. 
# We will be using stacks to make sure the parentheses are balanced in mathematical expressions 
# such as:  ((3^2+8)∗(5/2))/(2+6).  In real life you can see this extend to many things such as 
# text editor plugins and interactive development environments for all sorts of bracket completion 
# checks.

# Take a string as an input and return True if it's parentheses are balanced or False if it is not.



# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    # TODO: Intiate stack object
    equationStack = Stack()

    # TODO: Interate through equation checking parentheses
    for char in equation:
        if char == '(':
            equationStack.push(char)
        elif char == ')':
            if equationStack.pop() == None:
                return False
    
    # TODO: Return True if balanced and False if not
    if equationStack.size() == 0:
        return True
    else:
        return False
    
    pass

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")