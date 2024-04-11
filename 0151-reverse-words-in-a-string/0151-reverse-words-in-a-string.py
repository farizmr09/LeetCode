class Solution:
    def reverseWords(self, s: str) -> str:
        holder = []
        start = 0
        end = 0
        s = s.strip()

        for i in range(len(s)):
            if s[i] == " " and s[i - 1] != " ":
                end = i
                holder.append(s[start:end].strip())
                start = i
            if i == len(s) - 1:
                end = i
                holder.append(s[start:end + 1].strip())

        holder.reverse()
        return(" ".join(map(str, holder)))
    
        