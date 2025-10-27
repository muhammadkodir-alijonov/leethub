# len - 1 and second index must be skipped
# numRows = 1 we can just return s
# main logic:
# iterate through len of s and ever col finished just add in a new arr
# when finished case we can return a new arr to_string

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows  # har bir qatordagi harflarni saqlash
        cur_row = 0  # hozir qaysi qatordamiz
        going_down = False  # pastga ketyapmizmi yoki yuqoriga?

        if numRows == 1:
            return s
        for c in s:
            rows[cur_row] += c  # shu qatorga harfni qo‘shamiz

            # yo‘nalishni o‘zgartirish
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down  # tepa/pastni almashtiramiz

            # qaysi qatorga o‘tish
            cur_row += 1 if going_down else -1
        
        return ''.join(rows)