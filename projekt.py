from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

class SLESolver:
    def solveGenerator (self , inputFile , N, tol ):
        pass
    def solve (self , inputFile , outputFile , intermediateResultsFile , N, tol ):
        pass

class jacob(SLESolver):
    x = []
    A = []
    b = []
    line = 0
    def solveGenerator (self , inputFile , N , tol ):
        f = open(inputFile, "r")
        self.line=f.readline()
        size=(int(self.line), int(self.line))
        self.A = zeros(size)
        for i in range(int(self.line)):
            next=f.readline()
            next=next.replace("\n", "")
            temp=next.split(' ')
            for j in range(int(self.line)):
                self.A[i][j]=temp[j]
        self.b = zeros(int(self.line))
        for i in range(int(self.line)):
            next=f.readline()
            next=next.replace("\n", "")
            self.b[i]=next
        self.x = zeros(int(self.line))
        D = diag(self.A)
        R = self.A - diagflat(D)
        for i in range(N):
            self.x = (self.b - dot(R,self.x)) / D
            yield self.x
        f.close

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
        for i in range(0, int(self.line)):
            print( ' [ ', end=' ')
            for j in range(0, int(self.line)):
                print("{0:10.3e}".format(self.A[i][j]) , end=' ')
            print( ' ] ', end=' ')
            print('[ ' + '{0:10.3e}'.format(self.x[i]) + ' ] ' + ' = ' + ' [ ' + '{0:10.3e}'.format(self.b[i]) + ' ]')
        f2.close
        f3.close
        return ret

SLS=jacob()
sol = SLS.solve("input.txt", "output.txt", "inter.txt", 25, 0.001)
