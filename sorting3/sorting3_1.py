''' Lesson 3 solution. '''

def KnuthSequence(array_size : int) -> list[int]:
    ''' Forms sequence of steps for Shellsort. '''
    sequence : list[int] = [1] * array_size
    for next_step in range(len(sequence) - 2, -1, -1):
        sequence[next_step] = 3 * sequence[next_step + 1] + 1
    return sequence






