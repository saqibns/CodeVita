import random
rows = random.randrange(1, 100)
cols = random.randrange(1, 100)

f = open("C:\\Users\\Saqib\\Desktop\\mine_cases_full.txt", "w")
for dummy in xrange(100):
    f.write(str(rows) + " " + str(cols) + "\n")
    for i in xrange(rows):
        for j in xrange(cols):
            if random.randrange(12) <= 1:
                f.write("*")
            else:
                f.write(".")
        f.write("\n")
    rows = random.randrange(1, 10)
    cols = random.randrange(1, 10)

f.close()