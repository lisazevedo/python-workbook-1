from math import sqrt
from itertools import count, islice

def isPrime(n): return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def main(): print("Prime") if isPrime(int(input("Enter your value: "))) else print("Not it is prime")

if __name__ == "__main__": main()