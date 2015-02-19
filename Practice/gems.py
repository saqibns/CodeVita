rocks = int(input())

sets = list()
for dummy in range(rocks):
    sets.append(set(input()))

first = sets.pop()
for s in sets:
    first = first.intersection(s)

print(len(first))
