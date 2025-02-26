''' Lesson 2 solution. '''

def InsertionSortStep(array : list[int], step : int, i : int ) -> None:
    ''' ., '''
    for current_element_index in range(i, len(array), step):
        for sorted_element_index in range(current_element_index - step, i - 1, -step):
            if array[sorted_element_index] <= array[sorted_element_index + step]:
                break
            array[sorted_element_index + step], array[sorted_element_index] = \
                array[sorted_element_index], array[sorted_element_index + step]





