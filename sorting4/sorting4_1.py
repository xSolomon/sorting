''' Lesson 4 solution. '''

def ArrayChunk(M : list[int]) -> int:
    ''' Split array into two groups depending on pivot. '''
    while len(M) > 0:
        pivot_index : int = len(M) // 2
        pivot : int = M[pivot_index]
        left_part_index : int = 0
        right_part_index : int = len(M) - 1
        while left_part_index != right_part_index:
            while M[left_part_index] < pivot:
                left_part_index += 1
            while M[right_part_index] > pivot:
                right_part_index -= 1
            if left_part_index == right_part_index - 1 and \
                M[left_part_index] > M[right_part_index]:
                M[left_part_index], M[right_part_index] = M[right_part_index], M[left_part_index]
                break
            if left_part_index == right_part_index or \
                (left_part_index == right_part_index - 1 and \
                    M[left_part_index] < M[right_part_index]):
                return pivot_index
            M[left_part_index], M[right_part_index] = M[right_part_index], M[left_part_index]
    return None





