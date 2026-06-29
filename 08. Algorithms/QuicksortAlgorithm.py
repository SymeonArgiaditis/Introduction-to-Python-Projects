def quick_sort(array) -> list:
    if array == []:
        return []
    if len(array) <= 1:
        return array
    
    pivot_value = array[0]

    smaller_sublist = [element for element in array if element < pivot_value]
    equal_sublist = [element for element in array if element == pivot_value]
    greater_sublist = [element for element in array if element > pivot_value]

    return quick_sort(smaller_sublist) + equal_sublist + quick_sort(greater_sublist)

print(quick_sort([20, 3, 14, 1, 5]))