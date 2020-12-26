def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    temp=[]
    score=0
    count=0
    max_moves=0
    for i in range(len(a)):
        if score + a[-1] > x:
            break
        else :
            temp.append(a.pop())
            score+=temp[-1]
            count+=1
    max_moves=count
    for i in range(len(b)):
        score+=b.pop()
        count+=1
        while score >x and count>0 and len(temp)>0:
            score-=temp.pop()
            count-=1
        if(score<=x and count>max_moves):
            max_moves=count
    return max_moves
            
