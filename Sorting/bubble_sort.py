import time
starting_time = time.time()

def bubble_sort(list):
    """
    Worst case complexity of O(n)²
    """
    n = len(list)
    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):  
            # '-i' AS the last element is already sorted.
            next_item = j+1
            if list[j] > list[next_item]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True

        if swapped == False:
            break
    return list

if __name__ == '__main__':
    unsorted_list = [55, 4, 2, 7, 8, 32, 1, 1678, 3] #This is the list which will be sorted.
    sorted_list= bubble_sort(unsorted_list)
    print(sorted_list)
    print(f'Time used: {time.time() - starting_time}')
