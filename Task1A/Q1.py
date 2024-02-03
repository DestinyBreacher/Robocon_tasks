import math
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        for i in range(numRows):
            if i == 0:
                b=[1]
                a.append(b)
            else:
                b=[]
                for j in range(i):
                    b.append(math.comb(i,j))
                b.append(1)    
                a.append(b)
        return a