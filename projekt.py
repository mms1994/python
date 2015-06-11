from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

class SLESolver :
    def solveGenerator (self , inputFile , N , tol ):
        f = open(inputFile, "r")
        line=f.readline()
        size=(int(line), int(line))
        A = zeros(size)
        for i in range(int(line)):
            next=f.readline()
            next=next.replace("\n", "")
            temp=next.split(' ')
            for j in range(int(line)):
                A[i][j]=temp[j]
        b = zeros(int(line))
        for i in range(int(line)):
            next=f.readline()
            next=next.replace("\n", "")
            b[i]=next
        x = zeros(int(line))
        D = diag(A)
        R = A - diagflat(D)
        for i in range(N):
            x = (b - dot(R,x)) / D
            yield x

    def solve (self , inputFile , outputFile , intermediateResultsFile , N , tol ):
        gen = self.solveGenerator(inputFile, N, tol)
        f3 = open(intermediateResultsFile,  'w')
        for i in range(N):
            ret=next(gen)
            f3.write(str(i))
            f3.write(' ')
            for j in range(len(ret)):
                f3.write(str(ret[j]))
                f3.write(' ')
            f3.write('\n')
        f2 = open(outputFile, 'w')
        f2.write(str(len(ret)))
        f2.write('\n')
        for i in range(len(ret)):
            f2.write(str(ret[i]))
            f2.write(' ')
        return ret

SLS=SLESolver()
sol = SLS.solve("input.txt", "output.txt", "inter.txt", 25, 0.001)

print ("x:")
print(sol)