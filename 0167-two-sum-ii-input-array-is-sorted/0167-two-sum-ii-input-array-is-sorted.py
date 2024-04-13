class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(numbers)):
            holder = target - numbers[i]
            if numbers[i] in dict:
                return ([dict[numbers[i]] + 1, i + 1])     
            dict[holder] = i