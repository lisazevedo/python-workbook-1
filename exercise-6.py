from math import sqrt
from itertools import count, islice

# exercise 6
def isPrime(n): return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))
