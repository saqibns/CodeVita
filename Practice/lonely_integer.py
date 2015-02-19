def lonely(array, length):
    freq = dict()
    for i in range(length):
        freq[array[i]] = 0
    for i in range(length):
        freq[array[i]] += 1
    #print freq
    for key in freq:
        if freq[key] == 1:
            return key


def main():
    length = int(raw_input())
    numbers = map(int, raw_input().split())
    print lonely(numbers, length)

main()