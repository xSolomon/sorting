''' Lesson 3 solution. '''

def KnuthSequence(array_size : int) -> list[int]:
    ''' Forms sequence of steps for Shellsort. '''
    sequence : list[int] = []
    current_step : int = 1
    while current_step <= array_size:
        sequence.append(current_step)
        current_step = 3 * current_step + 1
    return sequence[::-1]






