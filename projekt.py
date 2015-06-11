from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

class SLESolver :
    def solveGenerator (self , inputFile , N , tol ):
        A = array([[10.0,0.0,-1.0],[1.0,5.0,0.0],[2.0,0.0,10.0]])
        b = array([1.0,2.0,3.0])
        x = array([1.0,1.0,1.0])
        x = zeros(len(A[0]))
        D = diag(A)
        R = A - diagflat(D)
        for i in range(N):
            x = (b - dot(R,x)) / D
            yield x

    def solve (self , inputFile , outputFile , intermediateResultsFile , N , tol ):
        pass


def jacobi(N):
    SLES=SLESolver()
    gen = SLES.solveGenerator("input.txt", N, 0.001)
    for i in range(N):
        ret=next(gen)
        print(ret)
    return ret
sol = jacobi(25)

print ("x:")
print(sol)