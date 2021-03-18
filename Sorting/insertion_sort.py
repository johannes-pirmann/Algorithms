import time

starting_time = time.time()

def insertion_sort(arr):
    """
    Worst complexity: O(N²)
    """
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [455, 2, 9, 76, 32, 11, 12209, 75, 97834, 54, 3, 4, 1, 76666, 2222, 12, 2345, 6] #Test Data

print(insertion_sort(arr))
print(f'Time: {time.time() - starting_time}')
