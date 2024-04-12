class Solution:
    def intToRoman(self, num: int) -> str:
        dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        holder = []
        def roman(num):
            for el in reversed(dict):
                if num >= el:
                    holder.append(int(num/el) * dict[el])
                    num = num - el * int(num/el)
                    print(num, el)
                    break
            if(num == 0):
                return num
            return roman(num)

        roman(num)
        return("".join(holder))
