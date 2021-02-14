def xor(n):
    if n%4==0:
        return n
    elif n%4==1:
        return 1
    elif n%4==2:
        return n+1
    else:
        return 0
def solution(start, length):
    checksum=0
    i=length
    while i>=1:
        checksum ^= xor(start-1)^xor(start+i-1)
        i-=1
        start+=length
    return checksum
print(solution(17,4))
