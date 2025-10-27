# len - 1 and second index must be skipped
# numRows = 1 we can just return s
# main logic:
# iterate through len of s and ever col finished just add in a new arr
# when finished case we can return a new arr to_string

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [''] * numRows
        i = 0
        d = 1

        for char in s:
            arr[i] += char
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        return ''.join(arr)