# Leap year or not using using if-elif-else statements

def isLeapYear(year):
  if(year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year =int(input("Enter a year : "))

if isLeapYear(year):
  print("\n{} is a leap year.".format(year))
else:
  print("\n{} is not a leap year.".format(year))
