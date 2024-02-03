class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lis=[0,0]
        for i in moves:
            if i == 'R':
                lis[0] = lis[0] + 1
            elif i == 'L':
                lis[0] = lis[0] - 1
            elif i == 'U':
                lis[1] = lis[1] + 1
            elif i == 'D':
                lis[1] = lis[1] - 1
        if lis == [0,0]:
            return True
        else:
            return False