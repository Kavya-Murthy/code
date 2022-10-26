def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = []
n = int(input("Enter size of array: "))
for i in range(n):
    num = int(input("Enter any number: "))
    arr.append(num)

print("Unsorted array is:\t")
for i in range(len(arr)):
    print(arr[i], end=" ")

insertionSort(arr)

print("\nSorted array is:\t")
for i in range(len(arr)):
    print(arr[i], end=" ")
