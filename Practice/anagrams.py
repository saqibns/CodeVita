one = input()
two = input()

first = sorted(list(one))
second = sorted(list(two))

i = 0
while first[i] == second[i]:
    i += 1

xs1 = len(first) - i
xs2 = len(second) - i
print(i)
print(xs1)
print(xs2)
print(xs1 + xs2)


