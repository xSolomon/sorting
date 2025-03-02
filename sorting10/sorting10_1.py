''' Lesson 10 solution. '''

class ksort():
    ''' Sorts values lexicographically in linear time.
        Value format: AMN, where:
        A = symbol from (a, b, c, d, e, f, g, h)
        MN = two digits '''
    def __init__(self):
        self.items : list[str] = [None] * (8 * pow(10, 2))

    def _hash(self, s : str) -> int:
        ''' Converts correct string into array index. '''
        # In UNICODE, 'a' = 97, '0' = 48
        return 100 * (ord(s[0]) - 97) + 10 * (ord(s[1]) - 48) + (ord(s[2]) - 48)

    def _is_valid_string(self, s : str) -> bool:
        ''' Determines whether provided string is valid. '''
        if len(s) != 3:
            return False
        if not (s[0] >= 'a' and s[0] <= 'h' and \
            s[1].isdigit() and \
            s[2].isdigit()):
            return False
        return True

    def index(self, s : str) -> int:
        ''' Returns index of string in array.
            Returns -1 if string format is incorrect. '''
        return self._hash(s) if self._is_valid_string(s) else -1

    def add(self, s : str) -> bool:
        ''' For valid string, adds it to array and returns true.
            Returns false if string is not valid. '''
        if not self._is_valid_string(s):
            return False
        self.items[self._hash(s)] = s
        return True





