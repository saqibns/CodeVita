SERIES = {
    0 : [0],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1],
    }

def main():
    test_cases = input()
    count = 1
    while count <= int(test_cases):
        count += 1
        line = input()
        numbers = line.split(' ')
        if int(numbers[1]) == 0:
            print(1)
        else:
            print(compute_last_digit(int(numbers[0]), int(numbers[1])))

def compute_last_digit(a, b):
    last_digit_a = a % 10
    digit_set = SERIES[last_digit_a]
    position = b % len(digit_set)
    return digit_set[position - 1]
main()


