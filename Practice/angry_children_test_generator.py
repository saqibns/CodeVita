f = open("angry_children.txt", "r")
lst = list()
for line in f:
    lst.append(int(line))

print lst[2:]