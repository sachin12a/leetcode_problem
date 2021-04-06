class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1 = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if(i in dict1):
                dict1[i] += 1
        dict1['l'] //= 2
        dict1['o'] //= 2
        return(min(list(dict1.values())))
