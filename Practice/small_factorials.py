def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

t = int(input())
count = 1
while count <= t:
    print(factorial(int(input())))
    count += 1

