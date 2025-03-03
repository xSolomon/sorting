''' Lesson 12 solution. '''

class BinarySearch():
    ''' Searches element in sorted array in log(N) time. '''
    def __init__(self, ary_sorted_ascending : list[int]):
        self._values = ary_sorted_ascending.copy() # List of ascending sorted values.
        self.Left : int = 0 # Left border.
        self.Right : int = len(self._values) - 1 # Right border.
        self._search_result : int = 0 # Current search status

    def Step(self, N : int) -> None:
        ''' Performs one step in searching value. '''
        if self._search_result != 0:
            return
        if not self._values:
            self._search_result = -1
            return
        middle_element_index : int = (self.Left + self.Right) // 2
        middle_element : int = self._values[middle_element_index]
        match (N > middle_element) - (N < middle_element):
            case 0:
                self.Left = self.Right = middle_element_index
                self._search_result = 1
                return
            case -1:
                self.Right = max(middle_element_index - 1, 0)
            case 1:
                self.Left = min(middle_element_index + 1, len(self._values) - 1)
        if self.Left + 1 < self.Right:
            return
        if self._values[self.Left] == N or self._values[self.Right] == N:
            self._search_result = 1
            return
        self._search_result = -1

    def GetResult(self) -> int:
        ''' Returns currect search status, where:
            0 = search continues
            1 = element found
            -1 = element not found '''
        return self._search_result

    def GallopingSearch(self, ary_sorted_ascending : list[int], search_value : int) -> bool:
        ''' Performs search with O(log(i)) complexity. '''
        if len(ary_sorted_ascending) < 1:
            return False
        i : int = 1
        current_index : int = 0
        while ary_sorted_ascending[current_index] < search_value:
            i += 1
            current_index = pow(2, i) - 2
            if current_index >= len(ary_sorted_ascending):
                current_index = len(ary_sorted_ascending) - 1
                i -= 1
                break
        if ary_sorted_ascending[current_index] == search_value:
            return True
        binary_searh : BinarySearch = BinarySearch(ary_sorted_ascending)
        binary_searh.Left = pow(2, i - 1) - 1
        binary_searh.Right = current_index
        while binary_searh.GetResult() == 0:
            binary_searh.Step(search_value)
        return binary_searh.GetResult() == 1









