import math

def hypotenuse(a, b):
  assert isinstance(a, int), "a must be a integer"
  assert isinstance(b, int), "b must be an integer"
  assert a >= 0, "a must be a positive number"
  assert b >= 0, "b must be a positive number"
  
  c = a**2 + b**2
  return math.sqrt(c)

print (hypotenuse(3, 4))