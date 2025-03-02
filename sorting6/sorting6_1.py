''' Lesson 6 solution. '''

def partition(values : list[int], left_border : int, right_border : int) -> int:
    ''' Split array values into two groups depending on pivot, and return pivot. '''
    while left_border < right_border:
        pivot_index : int = (right_border + left_border) // 2
        pivot : int = values[pivot_index]
        left_part_index = left_border
        right_part_index = right_border
        while left_part_index <= right_part_index:
            while values[left_part_index] < pivot:
                left_part_index += 1
            while values[right_part_index] > pivot:
                right_part_index -= 1
            if left_part_index == right_part_index - 1 and \
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

def QuickSort(array : list[int], recursion_stack : list[tuple[int, int]]) -> None:
    ''' Quicksort using partition function. '''
    if not recursion_stack:
        return
    borders : tuple[int, int] = recursion_stack.pop()
    if borders[0] >= borders[1]:
        return QuickSort(array, recursion_stack)
    pivot : int = partition(array, *borders)
    recursion_stack.append((borders[0], pivot - 1))
    recursion_stack.append((pivot + 1, borders[1]))
    return QuickSort(array, recursion_stack)

def QuickSortTailOptimization(array : list[int], left : int, right : int) -> None:
    ''' Hoare sorting with tail recursion via manually holding stack. '''
    QuickSort(array, [(left, right)])










