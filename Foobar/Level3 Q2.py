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
