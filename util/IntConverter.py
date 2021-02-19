# Marc F.
# 02/19/2021
# Int-Type Converter: Converts string-type values to integers, if possible.

# Functions & Input
## Classy function to convert it to an integer, including negatives.
def my_int(string):
  ### Preliminary setup of dictionary and required variables.
  numDict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
  intValue = 0
  negative = False

  ### Handling of any possible negative integer.
  if "-" in string:
    sliceVal_Neg = string.find("-")
    string = string[sliceVal_Neg+1:]
    negative = True
  ### Handling of any unneeded letters.
  if not string.isdecimal():
    #### Handling of decimals (including multiple decimals, and letters in decimals)
    if "." in string:
      sliceVal = string.find(".")
      decimal = string[sliceVal+1:]
      string = string[:sliceVal]
      
      if not decimal.isdecimal():
        return None
    if not string.isdecimal():
      return None
  ### Convert each decimal (using the multiples of 10 and dictionary conversion)
  for number in string:
    intValue = 10 * intValue + numDict[number]
  ### Add back the negative (if the integer was originally negative)
  if negative == True:
    intValue = intValue * -1
  return intValue

## Grab the input.
string = input("What number would you like returned as an int value? Go ahead. Try me.")

# Processing & Output
intValue = my_int(string)
print(intValue)