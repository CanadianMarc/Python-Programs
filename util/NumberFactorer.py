# Marc F.
# 02/16/2021
# Number Factorizer: Factorize numbers!
...
# Functions
## First Function: Calculate the factors of a number.
def calc_factors(number):
  factors = []
  for i in range(1, number+1):
    if number % i == 0:
      factors.append(i)

  return factors

## Second Function: Find the prime numbers in the factor list.
def prime_factors(factors):
  pFactors = []
  for factor in factors:
    factorList = calc_factors(factor)
    if len(factorList) == 2:
      pFactors.append(factorList[1])
  
  return pFactors

## Final Function: Get the prime factors for each number, if they exist.
def factorize(primes):
  pFactorized = []
  for prime in primes:
    term = num / prime
    remainder = term % prime
    if not prime == num:
      pFactorized.append(prime)
    loop = True

    while loop:
      remainder = term % prime
      term = term / prime
      if remainder == 0:
        pFactorized.append(prime)
      else:
        loop = False
  return pFactorized
    
# Input
num = int(input("May I have a number to factor, please?\n"))

# Processing
factors = calc_factors(num)
pFactors = prime_factors(factors)
pFactorized = factorize(pFactors)

# Output
print("\nGreat! Let's get this sorted for you.\nFactors:", factors, "\nFactors (Prime Numbers Only): ", pFactors, "\nPrime Factors: ", pFactorized)