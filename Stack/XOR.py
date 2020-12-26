def max_xor(arr):
    stack=[]
    ans=0
    for i in arr:
        while stack:
            top=stack[-1]
            temp=i^top
            if(temp>ans):
                ans=temp
            if(i<top):
                stack.pop()
            else:
                break
        stack.append(i)
    return ans
n=int(input())
l=list(map(int,input().split()))
print(max_xor(l))
