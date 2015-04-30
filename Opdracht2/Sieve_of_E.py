import sys
import time

N = int(sys.argv[1])
PrimeList = list(range(0,N+1))
PrimeList[1]=0
echtepriemgetallen = []
T1 = time.perf_counter()

primes = range(1, N+1)
for i in primes:
        factors = range(i, N+1, i)
        if PrimeList[i] !=0:
            echtepriemgetallen.append(PrimeList[i])
            for j in factors[1:]:
               PrimeList[j]=0

T2 = time.perf_counter() 

lengte = len(echtepriemgetallen)
print('Found', lengte, 'Prime numbers smaller than', int(sys.argv[1]), 'in', str(T2 - T1), 'sec.')

file = open(sys.argv[2], "w")

sep = ""
for x in echtepriemgetallen:
    file.write(sep + str(x))
    sep = "\n"
file.close()