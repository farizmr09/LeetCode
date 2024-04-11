class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s.reverse()
        s = [element for element in s if element != ""]
        return(" ".join(map(str, s)))
    
        