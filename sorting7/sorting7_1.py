''' Lesson 7 solution. '''

def KthOrderStatisticsStep(Array : list[int], L : int, R : int, k : int) -> list[int]:
    ''' Performs one step for finding Kth order statistics.
        Returns new borders to search in. '''
    if L < R or not Array:
        return []
    pivot_index : int = None
    search_finished : bool = False
    while not search_finished:
        pivot_index : int = (R + L) // 2
        pivot : int = Array[pivot_index]
        left_part_index = L
        right_part_index = R
        while left_part_index <= right_part_index:
            while Array[left_part_index] < pivot:
                left_part_index += 1
            while Array[right_part_index] > pivot:
                right_part_index -= 1
            if left_part_index == right_part_index - 1 and \
                Array[left_part_index] > Array[right_part_index]:
                Array[left_part_index], Array[right_part_index] = \
                    Array[right_part_index], Array[left_part_index]
                break
            if left_part_index == right_part_index or \
                (left_part_index == right_part_index - 1 and \
                    Array[left_part_index] < Array[right_part_index]):
                search_finished = True
                break
            Array[left_part_index], Array[right_part_index] = \
                Array[right_part_index], Array[left_part_index]
            if Array[left_part_index] == pivot:
                pivot_index = left_part_index
                continue
            if Array[right_part_index] == pivot:
                pivot_index = right_part_index
    match (k > pivot_index) - (k < pivot_index):
        case -1:
            return [L, pivot_index - 1]
        case 0:
            return [pivot_index, pivot_index]
        case 1:
            return [pivot_index + 1, R]










