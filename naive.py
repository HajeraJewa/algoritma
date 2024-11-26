import random
def naive_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

input_array = [random.randint(1, 100) for _ in range(50)]


sorted_array = naive_sort(input_array.copy())

print("Input Array (Unsorted):", input_array)
print("\nSorted Array:", sorted_array)
