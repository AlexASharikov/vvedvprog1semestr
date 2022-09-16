def Funk(K,N):
    return(K+N)
A,B,C = map(str, input().split())
V = Funk(B,A)

D = Funk(C,V)
print(D)
