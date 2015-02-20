def main():
    
    for i in range(10):
        print('Test', str(i + 1) + ':')
        length = input()
        expression = list(input())
        operations = int(input())
        for j in range(operations):
            operation = int(input())
            if operation == 0:
                check(expression)
            else:
                bracket = expression[operation - 1]
                if bracket == '(':
                    expression[operation - 1] = ')'
                else:
                    expression[operation - 1] = '('

def check(expression):
    stack = 0
    for i in expression:
        if i == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            break
    if stack == 0:
        print('YES')
    else:
        print('NO')
    

main()

