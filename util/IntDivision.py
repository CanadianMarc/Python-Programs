# Marc F.
# 02/19/2021
# Integer Division: Divide numbers to get back the whole integer and any possible remainders

# Functions
def int_div(dividend, divisor):
  result = 0
  while dividend >= divisor:
    dividend = dividend - divisor
    result = result + 1
  return result

def my_mod(dividend, divisor):
  while dividend >= divisor:
    dividend = dividend - divisor
    
  if dividend < divisor:
    counter = dividend
    return counter

# Input
dividend = int(input("What number are you starting out with?\n"))
divisor = int(input("What number would you like to divide by?\n"))
print("\nGreat! Let me calculate this for you really quick...")

# Processing
intDivision = int_div(dividend, divisor)
modDivision = my_mod(dividend, divisor)

# Output
print("The results are IN! Are you ready for them?\nDivision: " + str(intDivision) + "\nRemainder: " + str(modDivision))