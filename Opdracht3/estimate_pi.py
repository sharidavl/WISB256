import random
import sys
import math

if len(sys.argv) > 3:
    random.seed(float(sys.argv[3]))

if len(sys.argv) < 3:
    print("Use: estimate_pi.py N L")
    exit(1)

N = int(sys.argv[1])
L = float(sys.argv[2])

if L > 1:
    print("AssertionError: L should be smaller than 1")
    exit(1)

def drop_needle(L):
        x0 = random.random()
        theta = random.vonmisesvariate(0,0)
        x1 = x0 + L*math.cos(theta)
        if x1 >= 1 or x1 <= 0:
            return True
        else:
            return False 

i = 0
hits = 0
while i < N:
    if drop_needle(L) == True:
        hits = hits + 1
    i = i + 1
    
print(hits, "hits in", N, "tries")
print("Pi =", 2*L/(hits/N))