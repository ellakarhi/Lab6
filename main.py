def is_leapyear(year):
  if year % 100 == 0:
    return True
    if year % 400 == 0:
      return True
    else:
      return False
      
  elif year % 4 == 0:
    if year % 100 == 0:
      if year % 400 != 0:
       return False
  elif year % 4 == 0:
    if year % 100 != 0:
      return False
  else:
    return False
print (is_leapyear(4))