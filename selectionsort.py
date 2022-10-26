def selectionSort(A):
    for i in range(len(A)):
        min_idx = i

        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]


arr = []
n = int(input("Enter size of array: "))
for i in range(n):
    num = int(input("Enter any number: "))
    arr.append(num)

print("Unsorted array is:\t")
for i in range(len(arr)):
    print(arr[i], end=" ")

selectionSort(arr)

print("\nSorted array is:\t")
for i in range(len(arr)):
    print(arr[i], end=" ")
