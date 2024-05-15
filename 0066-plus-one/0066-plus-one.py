class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i] + 1) // 10 == 0:
                digits[i] = (digits[i] + 1) % 10
                break
            elif i == 0:
                digits[i] = (digits[i] + 1) % 10
                digits.insert(0, 1)
            else:
                digits[i] = (digits[i] + 1) % 10
        return digits