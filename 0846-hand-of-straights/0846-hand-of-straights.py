class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)/groupSize > int(len(hand)/groupSize):
            return False
        for i in range(len(hand)//groupSize):
            holder = list(set(hand))
            holder.sort()
            for j in range(groupSize):
                if len(holder) < groupSize:
                    return False
                if j - 1 >= 0 and holder[j] - holder[j - 1] != 1:
                    return False
                hand.remove(holder[j])
        return True

