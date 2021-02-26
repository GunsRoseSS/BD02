# pseudocode BD02 Richard en Bas
#
# Opdracht 1: sorteer een lijst dmv decrease and conquer
unsortedlist = []


def InsertionSort(A, i):
    current = A[i]
    j = i - 1
    while j >= 0 and A[j] > current:
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = current
    print("insertion:", A)
    return A


B = []


def dsort(A, B):
    if len(A) == 0:
        return B
    else:
        B.append(A[0])
        A.pop(0)
        B = InsertionSort(B, len(B) - 1)
        print(A, "  ", B)
        return dsort(A, B)


print(dsort([88, 6, 4, 72, 1], B))

# [5, 4, 1]
# [1, 5, 4]
# [5, 4]
