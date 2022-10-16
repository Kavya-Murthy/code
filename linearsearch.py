def linear_search(arr, x):
    c = 0
    for i in range(len(arr)):
        if arr[i] == x:
            c += 1

    if c == 0:
        print(f"Element {x} is not present in array")
    else:
        print(f"Element {x} is present at index {i}")


arr = [9, 17, 52, 10, 7, 77]
x = 7
linear_search(arr, x)