from math import gcd
from fractions import Fraction
def dot(A,B):
    return [[sum(a*b for a,b in zip(A_row,B_col))for B_col in zip(*B) ]for A_row in A]

def inv( A):

    d = det(A)
    if len(A) == 2:
        return [[A[1][1]/d, -1*A[0][1]/d],
                [-1*A[1][0]/d, A[0][0]/d]]
    adj=transpose([[((-1)**(i+j))*det(minor(A,i,j)) for j in range(len(A))] for i in range(len(A))])
    return [[adj[i][j]/d for j in range(len(A))] for i in range(len(A))]

def det(A):
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    _det = 0
    for i in range(len(A)):
        _det += ((-1)**i)*A[0][i]*det(minor(A,0,i))
    return _det

def transpose(A):
    return [[i for i in col] for col in zip(*A)]

def minor(A, i, j):
     return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]

def identity(size):
    return [[0 if i!=j else 1 for j in range(size)] for i in range(size)]

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A))]for i in range(len(B))]

def prob(m):
    for i in range(len(m)):
        d=sum(m[i])
        if d:
            for j in range(len(m[i])):
                m[i][j]/=d

def lcm(denominators):
    l=denominators[0]
    for i in denominators[1:]:
        l=l*i//gcd(l,i)
    return l

def solution(m):
    prob(m)
    terminal={i for i in range(len(m)) if not max(m[i])}
    r=[[m[i][j] for j in range(len(m[0])) if j in terminal] for i in range(len(m)) if i not in terminal]
    q=[[m[i][j] for j in range(len(m[0])) if j not in terminal] for i in range(len(m)) if i not in terminal]
    f=inv(sub(identity(len(q)),q))
    fr=dot(f,r)
    ans=[Fraction(str(num)).limit_denominator()for num in fr[0]]
    LCM=lcm([fac.denominator for fac in ans])
    return [i.numerator *(LCM//i.denominator) for i in ans ]+[LCM]
m=[[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(solution(m))
