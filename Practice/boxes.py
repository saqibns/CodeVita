tests = int(input())
maxi = 0
for i in range(tests):
    mice, holes = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    n.sort()
    m.sort()
    for i in range(mice):
        mou = n[i]
        mini = abs(mou - m[0])
        idx = 1
        for j in range(holes):
            diff = abs(mou - m[j])
            if diff <= mini:
                mini = diff
            else:
                break
        if mini > maxi:
            maxi = mini
print(maxi)




