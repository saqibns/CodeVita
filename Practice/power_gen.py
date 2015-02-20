def go():
    for j in range(1, 20):
        print(j, ':')
        print()
        for i in range(1, 10):
            print((j ** i) % 10)
        print()


print((17979 ** 10) % 10)
print((69999 ** 2000) % 10)


