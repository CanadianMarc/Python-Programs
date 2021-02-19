# Marc F.
# 02/18/2021
# Int-Type Converter: Converts string-type values to integers, if possible.

# Functions & Input
## Classy function to convert it to an integer, including negatives.
def my_int(string):
  numDict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
  intValue = 0
  negative = False

  if "-" in string:
    sliceVal_Neg = string.find("-")
    string = string[sliceVal_Neg+1:]
    negative = True

  if not string.isdecimal():
    if "." in string:
      sliceVal = string.find(".")
      string = string[:sliceVal]
      
    if not string.isdecimal():
      intValue = None
      return intValue

  for number in string:
    intValue = 10 * intValue + numDict[number]

  if negative == True:
    intValue = intValue * -1
  return intValue

## Grab the input.
string = input("What number would you like returned as an int value? Go ahead. Try me.")

# Processing & Output
intValue = my_int(string)
print(intValue)