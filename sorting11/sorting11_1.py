''' Lesson 11 solution. '''

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
                self.Right = middle_element_index - 1
            case 1:
                self.Left = middle_element_index + 1
        if self.Left < self.Right:
            return
        if self.Left == self.Right and self._values[self.Left] == N:
            self._search_result = 1
            return
        self._search_result = -1

    def GetResult(self) -> int:
        ''' Returns currect search status, where:
            0 = search continues
            1 = element found
            -1 = element not found '''
        return self._search_result










