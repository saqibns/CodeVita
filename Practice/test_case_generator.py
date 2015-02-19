import random
RANGE_LOWER = 1
RANGE_UPPER = 100000
NO_OF_TESTS = 500

f = open("C:\\Users\\Saqib\\Desktop\\rand_tests.txt", "w")
for i in xrange(500):
        f.write(str(random.randrange(RANGE_LOWER, RANGE_UPPER)))
        f.write(" ")
        f.write(str(random.randrange(RANGE_LOWER, RANGE_UPPER)))
        f.write("\n")

f.close()
