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
