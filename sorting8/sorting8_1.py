''' Lesson 8 solution. '''

def MergeSort(values : list[int]) -> list[int]:
    ''' Performs classic ascending merge sort. '''
    if len(values) <= 1:
        return values
    middle_element_index : int = len(values) // 2
    first_part : list[int] = MergeSort(values[:middle_element_index])
    second_part : list[int] = MergeSort(values[middle_element_index:])
    result : list[int] = []
    first_part_index = 0
    second_part_index = 0
    while first_part_index < len(first_part) and second_part_index < len(second_part):
        if first_part[first_part_index] < second_part[second_part_index]:
            result.append(first_part[first_part_index])
            first_part_index += 1
            continue
        result.append(second_part[second_part_index])
        second_part_index += 1
    result.extend(first_part[first_part_index:len(first_part)] if \
        first_part_index < len(first_part) else \
        second_part[second_part_index:len(second_part)])
    return result








