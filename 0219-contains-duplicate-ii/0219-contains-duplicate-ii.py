class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]].append(i)
                if len(dict[nums[i]]) > 2:
                    dict[nums[i]].remove(dict[nums[i]][0])
                if abs(dict[nums[i]][0] - dict[nums[i]][1]) <= k:
                    return(True)
                    break
                continue 
            dict[nums[i]] = [i]
        return False