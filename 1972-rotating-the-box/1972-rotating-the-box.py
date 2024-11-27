from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            empty_index = len(row) - 1 
            for col in range(len(row) - 1, -1, -1):
                if row[col] == '*':
                    empty_index = col - 1
                elif row[col] == '#':  
                    row[col], row[empty_index] = '.', '#'
                    empty_index -= 1

        rotated_box = []
        m = len(box)
        n = len(box[0])
        for i in range(n):  
            new_row = [] 
            for j in range(m):
                new_row.append(box[m - 1 - j][i])
            rotated_box.append(new_row)  

        return rotated_box
