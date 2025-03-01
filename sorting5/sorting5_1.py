''' Lesson 5 solution. '''

def partition(values : list[int], left_border : int, right_border : int) -> int:
    ''' Split array values into two groups depending on pivot, and return pivot. '''
    while left_border < right_border:
        pivot_index : int = (right_border - left_border) // 2
        pivot : int = values[pivot_index]
        left_part_index = left_border
        right_part_index = right_border
        while values[left_part_index] < pivot:
            left_part_index += 1
        while values[right_part_index] > pivot:
            right_part_index -= 1
        if left_part_index == right_part_index and \
            values[left_part_index] > values[right_part_index]:
            values[left_part_index], values[right_part_index] = \
                values[right_part_index], values[left_part_index]
            break
        if left_part_index == right_part_index or \
            (left_part_index == right_part_index - 1 and \
                values[left_part_index] < values[right_part_index]):
            return pivot_index
        values[left_part_index], values[right_part_index] = \
            values[right_part_index], values[left_part_index]
        if values[left_part_index] == pivot:
            pivot_index = left_part_index
            continue
        if values[right_part_index] == pivot:
            pivot_index = right_part_index
    return None


def QuickSort(array : list[int], left : int, right : int) -> None:
    ''' Quicksort using partition function. '''
    if left == right:
        return
    pivot : int = partition(array, left, right)
    QuickSort(array, left, pivot - 1)
    QuickSort(array, pivot + 1, right)
