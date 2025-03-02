''' Lesson 9 solution. '''

class Heap:
    ''' Binary heap. '''
    def __init__(self):
        self.HeapArray : list[int] = [] # Stores non-negative numbers-keys.
        self.heap_depth : int = 0 # Heap depth level.
        self.first_free_index : int = 0 # First index that is free for inserting.

    def MakeHeap(self, a : list[int], depth : int) -> None:
        ''' Makes heap from given array by calling Add for each element. '''
        self.heap_depth = depth
        self.HeapArray = [None] * (pow(2, depth + 1) - 1)
        self.first_free_index = 0
        for _, key in enumerate(a):
            self.Add(key)

    def GetMax(self) -> int:
        ''' Return value contained in root, rebuilding heap via sift down. '''
        if self.size() == 0: # Heap is empty.
            return -1
        deleted_key : int = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.first_free_index - 1]
        self.HeapArray[self.first_free_index - 1] = None
        self.first_free_index -= 1
        if self.first_free_index == 0: # Deleted last element in heap.
            return deleted_key
        current_index : int = 0
        for _ in range(self.heap_depth):
            left_child_index : int = 2 * current_index + 1
            right_child_index : int = 2 * current_index + 2
            left_value : int = -1 if self.HeapArray[left_child_index] is None \
                else self.HeapArray[left_child_index]
            right_value : int = -1 if self.HeapArray[right_child_index] is None \
                else self.HeapArray[right_child_index]
            max_value : int = max(left_value, right_value)
            if max_value <= self.HeapArray[current_index]:
                return deleted_key
            index_to_swap : int = left_child_index if max_value == left_value else right_child_index
            self.HeapArray[current_index], self.HeapArray[index_to_swap] = \
            self.HeapArray[index_to_swap], self.HeapArray[current_index]
            current_index = index_to_swap
        return deleted_key

    def Add(self, key : int) -> bool:
        ''' Adds element to the heap, sifting it up.
            Returns false if heap is full. '''
        if self.first_free_index == len(self.HeapArray): # Heap if full.
            return False
        if key is None: # Nothing to add.
            return
        if key < 0: # Only non-negative keys are valid.
            return False
        self.HeapArray[self.first_free_index] = key
        current_index : int = self.first_free_index
        self.first_free_index += 1
        for parent_index in range(self.heap_depth + 1):
            parent_index = (current_index - 1) // 2
            if parent_index < 0 or self.HeapArray[parent_index] >= self.HeapArray[current_index]:
                return True
            self.HeapArray[parent_index], self.HeapArray[current_index] = \
                self.HeapArray[current_index], self.HeapArray[parent_index]
            current_index = parent_index
        return True

    def is_correct(self) -> bool:
        ''' Returns True if heap is correct (parent key is greater-equal than children keys). '''
        for node_index, parent_key in enumerate(self.HeapArray):
            if parent_key is None:
                continue
            left_child_index : int = node_index * 2 + 1
            if left_child_index < len(self.HeapArray) and \
                self.HeapArray[left_child_index] is not None and \
                parent_key < self.HeapArray[left_child_index]:
                return False
            right_child_index : int = node_index * 2 + 2
            if right_child_index < len(self.HeapArray) and \
                self.HeapArray[right_child_index] is not None and \
                parent_key < self.HeapArray[right_child_index]:
                return False
        return True

    def size(self) -> int:
        ''' Returns number of keys stored. '''
        return self.first_free_index

class HeapSort():
    ''' Heap sort using self-made heap class. '''
    def __init__(self, values : list[int]):
        self.HeapObject : Heap = Heap() # Heap object.
        heap_depth : int = 0
        heap_size_plus_one : int = 2
        while len(values) > heap_size_plus_one - 1:
            heap_depth += 1
            heap_size_plus_one *= 2
        self.HeapObject.MakeHeap([], heap_depth)
        for value in values:
            self.HeapObject.Add(value)

    def GetNextMax(self) -> int:
        ''' Pop and return max value in heap.
            Returns -1 if no such value. '''
        return self.HeapObject.GetMax()








