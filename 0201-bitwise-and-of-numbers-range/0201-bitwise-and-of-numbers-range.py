class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        
        if left == 0 or right == 0:
            return 0
        
        power = 1
        while power < left:
            power <<= 1
        
        if power <= right and power >= left:
            while power <= right:
                left &= power
                power *= 2
        else:
            for i in range(right, left, -1):
                left &= i
                
        
        return left