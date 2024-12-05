class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False

        start_non_underscore = start.replace('_', '')
        target_non_underscore = target.replace('_', '')

        if start_non_underscore != target_non_underscore:
            return False

        i, j = 0, 0
        n = len(start)

        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                break

            if start[i] != target[j]:
                return False

            if start[i] == 'L' and i < j: 
                return False
            if start[i] == 'R' and i > j:  
                return False

            i += 1
            j += 1

        return True
