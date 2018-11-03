#Programming of differential equations
"""
Class Hello:
    def __call__(self,name):
        return ('Hello '+ name)

    def __str__(self):
        return ('Hello World!')
"""
"""
Class Sum:
    def __init__(self, fk, M, N):
        self.term = fk
        self.M = M
        self.N = N

    def __call__(self, x):
        s = 0
        for k in range(self.M, self.N+1):
            s += self.term(k, x)
        return s

def term (k, x):
    return (-x)**k

S = Sum(term, M=0, N=3)
x = 0.5
print(S(x))
print(S.term(k=4, x=x))
"""

