def selection_sort(arr):
    min = arr[j]
    for j in range(len(arr)):
        for i in range(1,len(arr)):
            if arr[i] < min:
