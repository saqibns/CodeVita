def swap(m, n, array, length):
    idx = 1
    while idx < length:
        if array[idx] == m:
            array[idx] = n
        elif array[idx] == n:
            array[idx] = m
        idx += 1

def islands(array, length):
    idx = 0
    count = 0
    while idx < length - 1:
        if not (array[idx]) and array[idx + 1]:
            count += 1
        idx += 1
    return count

def construct(num, length, numbers):
    array = [numbers[i] <= num for i in range(1, length)]
##    print([False] + array)
    return [False] + array

def main():
    l, q = map(int, input().split())
    seq = [0] + list(map(int, input().split()))
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            swap(query[1], query[2], seq, l + 1)
        else:
            print(islands(construct(query[1], l + 1, seq), l + 1))

main()
