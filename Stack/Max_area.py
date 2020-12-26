def largestRectangle(height):
    hs=[]
    ps=[]
    maxarea=0
    height.append(0)
    for i in range(len(height)):
        last=len(height)+1
        while len(hs)!=0 and hs[-1]>height[i]:
            last=ps[-1]
            area=(i-ps.pop())*hs.pop()
            maxarea=max(maxarea,area)
        if len(hs)==0 or hs[-1]<height[i]:
            hs.append(height[i])
            ps.append(min(last,i))
    print(maxarea)
n=int(input())
l=list(map(int,input().split()))
largestRectangle(l)
