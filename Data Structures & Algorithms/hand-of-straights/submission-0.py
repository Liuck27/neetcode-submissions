class Solution:

    from collections import Counter
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()
        
        for elem in hand:
            if count[elem] == 0:
                continue
            else:
                for num in range(elem, elem+groupSize):
                    if count[num] == 0:
                        return False
                    else:
                        count[num] -= 1

        return True

