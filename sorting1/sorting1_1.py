''' Lesson 1 solution. '''

def SelectionSortStep( array : list[int], i : int ) -> None:
    ''' Finds minimum in unsorted part and inserts it at the end of sorted part. '''
    current_minimum_index : int = i
    for unsorted_index in range(i + 1, len(array)):
        if array[unsorted_index] < array[current_minimum_index]:
            current_minimum_index = unsorted_index
    array[i], array[current_minimum_index] = array[current_minimum_index], array[i]

def BubbleSortStep( array ):
    ''' Swap elements if current greater than next.
        Tracks whether any swaps occured. '''
    swaps_not_occured : bool = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swaps_not_occured = False
    return swaps_not_occured






