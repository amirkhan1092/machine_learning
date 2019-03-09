
# enumerate()
import itertools
def mul(i,j):
    return i*j
g=[1,34,6,32,0,65]

h=list(itertools.accumulate(g,mul))

print(h)
