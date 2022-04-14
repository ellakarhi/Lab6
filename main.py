def is_leapyear(year):
  if year % 4:
   return True 
  elif year % 100:
    return True
    if year % 400:
      return True
    else:
      return False
print (is_leapyear(2000))