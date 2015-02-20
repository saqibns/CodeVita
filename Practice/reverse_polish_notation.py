PRIORITY = {
    '+' : 1,
    '-' : 2,
    '*' : 3,
    '/' : 4,
    '^' : 5,
    '(' : 0
    }

SPECIAL = {'+', '-', '*', '/', '^', '(', ')'}

def main():
    """
    The function scans the input and passes it to the function to
    generate the reverse polish notation form
    """

    # Scan the number of test cases
    count = 1
    test_cases = int(input())
    while count <= test_cases:
        line = input()
        print(converter(line))
##        print(lower_limit)
##        print(upper_limit)
        
        count += 1

def converter(infix):
    stack = list()
    output = str()
    # For every character in the input
    for char in infix:

        if char not in SPECIAL:

            # If the character is a variable, add it to the output
            output += char
        else:
            # Otherwise, if the stack is empty, add the special symbol onto the stack
            if len(stack) == 0:
                stack.append(char)
            else:

                if char != '(' and char != ')':

                    # If the special symbol is an operator and its priority is higher than that of the symbol underneath, add it onto the stack otherwise keep popping the symbols of higher
                    # priority and push the current symbol on to the stack
                    
                    if PRIORITY[char] > PRIORITY[stack[-1]]:
                        stack.append(char)
                    else:
                        while len(stack) > 0 and PRIORITY[char] < PRIORITY[stack[-1]] and (stack[-1] != ')' or stack[-1] != '('):
                            output += stack.pop()
                        stack.append(char)
                # In case if any of the parenthesis is encountered, perform the operations related to parenthesis
                elif char == '(':

                    # If an opening parenthesis is encountered, push it on to the stack
                    stack.append('(')
                else:

                    # If a closing parenthesis is encountered, keep popping the symbols off the stack until an opening parenthesis is encountered and add it to the output
                    extract = stack.pop()
                    while extract != '(':
                        output += extract
                        extract = stack.pop()

    # Pop all the symbols from the stack after the input scanning is over and add the symbols to the result                 
    while len(stack) > 0:
        output += stack.pop()

    # Return the output
    return output

main()
    
