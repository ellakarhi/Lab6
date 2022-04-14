def is_numeric(num):
  """returns true is number is a int or a float"""
  return isinstance(num, int) or isinstance(num,float)

print (is_numeric(3))