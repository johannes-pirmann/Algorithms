import time
starting_time = time.time()

def bubble_sort(list):
    """
    Worst case complexity of O(n)²
    """
    for i in range(0, len(list)-1):
        swapped = False
        for j in range(0, len(list)-1):
            next_item = j+1
            if list[j] > list[next_item]:
                tmp = list[j]
                list[j] = list[next_item]
                list[j+1] = tmp
                swapped = True

        if swapped == False:
            break
    return list

if __name__ == '__main__':
    unsorted_list = [55, 4, 2, 7, 8, 32, 1, 1678, 3] #This is the list which will be sorted.
    sorted_list= bubble_sort(unsorted_list)
    print(sorted_list)
    print(f'Time used: {time.time() - starting_time}')
