from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n_boxes = list(boxes)
        ans = []
        for i, b in enumerate(n_boxes):
            fw = self.forward(n_boxes, i)
            bw = self.backward(n_boxes, i)
            ans.append(fw + bw)
        return ans

    def forward(self, n_boxes, i):
        summ = 0
        for b in range(i + 1, len(n_boxes)): 
            if n_boxes[b] == '1':
                summ += b - i
        return summ

    def backward(self, n_boxes, i):
        summ = 0
        for b in range(i - 1, -1, -1):
            if n_boxes[b] == '1':
                summ += i - b
        return summ

if __name__ == "__main__":
    solution = Solution()
    boxes = "001011"
    result = solution.minOperations(boxes)
    print(result)
