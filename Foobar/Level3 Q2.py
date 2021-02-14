"""
Doomsday Fuel
=============
Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as
raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may
be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.
Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state
of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions
it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each
time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).
You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms
that the ore can become, but you haven't seen all of them.
Write a function answer(m) that takes an array of array of non-negative ints representing how many times that state
has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in
simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a
path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The
ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the
fraction is simplified regularly.
For example, consider the matrix m:
[
    [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
    [0,0,0,0,0,0],  # s3 is terminal
    [0,0,0,0,0,0],  # s4 is terminal
    [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].""" 
from fractions import Fraction, gcd

# Matrix functions:


def dot(A, B):  # Matrix Multiplication
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


def inv(A):  # Inverse of Matrix
    d = det(A)
    if len(A) == 2:
        return [[A[1][1] / d, -1 * A[0][1] / d],
                [-1 * A[1][0] / d, A[0][0] / d]]

    adj = transpose([[((-1)**(i + j)) * det(minor(A, i, j))
                      for j in range(len(A))] for i in range(len(A))])
    return [[adj[i][j] / d for j in range(len(A))] for i in range(len(A))]


def det(A):  # Calculating inverse of matrix
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    _det = 0
    for i in range(len(A)):
        _det += ((-1)**i) * A[0][i] * det(minor(A, 0, i))
    return _det


def transpose(A):  # Caculate transpose of a matrix
    return [[i for i in col] for col in zip(*A)]


def minor(A, i, j):  # Returs minor of matrix A at i,j
    return [row[:j] + row[j + 1:] for row in (A[:i] + A[i + 1:])]


def identity(size):  # Returns identity matrix of given size
    return [[0 if i != j else 1 for j in range(size)] for i in range(size)]


def sub(A, B):  # Returns subtraction of two matrix A and B`
    return [[A[i][j] - B[i][j] for j in range(len(A))]for i in range(len(B))]


def prob(m):  # Converts the matrix entries to its corresponding probabilities
    for i in range(len(m)):
        d = sum(m[i])
        if d:
            for j in range(len(m[i])):
                m[i][j] /= float(d)


def lcm(denominators):  # Returns the LCM of a given list of numbers
    l = denominators[0]
    for i in denominators[1:]:
        l = l * i // gcd(l, i)
    return l


def solution(m):
    prob(m)
    # Find the terminal states in the given transistion matrix
    terminal = {i for i in range(len(m)) if not max(m[i])}
    # SPECIAL CASE
    # When there's only one terminal state, the given ore can only go there
    if len(terminal) == 1:
        return [1, 1]
    # Calculating R and Q matrices (Sub-Matrices) for Absolute Markov Chain calculation
    r = [[m[i][j] for j in range(len(m[0])) if j in terminal]
         for i in range(len(m)) if i not in terminal]
    q = [[m[i][j] for j in range(len(m[0])) if j not in terminal]
         for i in range(len(m)) if i not in terminal]
    # Calculating the Fundamental Matrix of the transistion matrix
    F = inv(sub(identity(len(q)), q))
    FxR = dot(F, r)
    Probabs =  [Fraction(str(num)).limit_denominator()for num in FxR[0]]
    LCM = lcm([fac.denominator for fac in Probabs])
    # Converting probabilities of elements into the required formatting
    return [i.numerator * (LCM // i.denominator) for i in Probabs] + [LCM]
m=[[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(solution(m))
