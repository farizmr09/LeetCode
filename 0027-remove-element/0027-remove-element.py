class Solution(object):
    def removeElement(self, nums, val):
        try: 
            while True:
                nums.remove(val)
        except:
            print(nums)
