import random
def conquer_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left = arr[:mid]    
        right = arr[mid:] 

        conquer_sort(left)
        conquer_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

input_array = [random.randint(1, 100) for _ in range(50)]
sorted_array = conquer_sort(input_array.copy())


print("Input Array (Unsorted):", input_array)
print("\nSorted Array (Merge Sort):", sorted_array)
