# Mergesort algorithm

def merge(list1, list2):
    i, j = 0, 0
    l1, l2 = len(list1), len(list2)

    new = list()
    while i < l1 and j < l2:
        if list1[i] == list2[j]:
            new.append(list1[i])
            new.append(list2[j])
            i += 1
            j += 1

        elif list1[i] > list2[j]:
            new.append(list2[j])
            j += 1

        else:
            new.append(list1[i])
            i += 1
    new.extend(list1[i :])
    new.extend(list2[j :])
    return new

def mergesort(listt):
    length = len(listt)
    if length == 0 or length == 1:
        return listt
    first = mergesort(listt[:length // 2])
    second = mergesort(listt[length // 2:])
    return merge(first, second)

#Tests for MergeSort
print "MergeSort:"
print mergesort([])
print mergesort([-73, 25, 66, 16, -25, 25, 68, 85, 90, -63, -46, 65])
print mergesort([8, -46, 0, -95, -30, 88, 26, -64])
print

# Quicksort algorithm

def partition(a, p, q):
    pivot = a[q]
    i = p - 1
    for j in range(p, q):
        if a[j] < pivot:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, q)
    return i + 1

def swap(listt, i , j):
    temp = listt[i]
    listt[i] = listt[j]
    listt[j] = temp

def quicksort(a, p, q):
    if p < q:
        r = partition(a, p, q)
        quicksort(a, p, r - 1)
        quicksort(a, r + 1, q)


#Tests for QuickSort
print "QuickSort:"
a = []
quicksort(a, 0, 0)
print a

a = [7, 50, -55, -20, 65, -79, 59, -98]
quicksort(a, 0, 7)
print a

a = [41, 10, 94, 92, 18, 22, -70, -60, -36, 85]
quicksort(a, 2, 7)
print a

print
