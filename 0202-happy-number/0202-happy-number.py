class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        if n == 1:
            return(True)
        while n != 1:
            n_split = list(str(n))
            n = sum(int(i)**2 for i in n_split)
            if dict.get(n) == None:
                dict[n] = 1
                continue
            return(False)
        return True