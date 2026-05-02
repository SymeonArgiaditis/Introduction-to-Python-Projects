def quick_sort_inplace(array): 

    def recursive_helper(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)

            recursive_helper(items, low, pivot_index)
            recursive_helper(items, pivot_index + 1, high)
        
        recursive_helper(array, 0, len(array) - 1)

        return array
    
def partition(items, low, high):
    pivot = items[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while items[i] < pivot:
            i += 1

        j -= 1
        while items[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        #Swap elements
        items[i], items[j] = items[j], items[i]

my_array = [4, 10, 6, 14, 2, 1, 8, 5]
quick_sort_inplace(my_array)
print(my_array)