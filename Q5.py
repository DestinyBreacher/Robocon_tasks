class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        lis=[]
        lis2=[]
        for i in range(1, area+1):
            if area%i == 0:
                lis.append(i)
                lis.append(area/i)
        min = lis[1] - lis[0]
        if min < 0:
            min = min*-1
        for j in range(0,len(lis),2):
            if lis[j+1] - lis[j] < 0:    
                if (-1)*(lis[j+1] - lis[j]) <= min:
                    min = lis[j+1] - lis[j]
                    lis2 = [int(lis[j+1]), int(lis[j])]
            else:
                if lis[j+1] - lis[j] <= min:
                    min = lis[j+1] - lis[j]
                    lis2 = [int(lis[j+1]), int(lis[j])]
        lis2.sort(reverse = True)
        return lis2