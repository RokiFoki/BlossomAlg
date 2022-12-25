from main import arePairs

def testPairs(a,b, expected):
  print(arePairs(a,b) == expected, a, b, arePairs(a,b), )

# testPairs(1,1, False)
# testPairs(1,2, True)
# testPairs(1,3, False)
# testPairs(2,3, True)
# testPairs(1,4, True)
# testPairs(1,5, True)
# testPairs(1,6, True)
# testPairs(1,7, False)
# testPairs(1,8, True)
# testPairs(1,9, True)
# testPairs(1,10, True)
# testPairs(pow(2, 30)-1,2, True)
# testPairs(107371823,4732621, True)


import random

def arePairs2(a, b): 
  if a == b: return False
  if (a + b) & 1:
    return True

  left = min(a,b)
  right = max(a,b)

  total = left + right
  if (total & 1):
    return True

  current = 0
  half = total
  while True:
    if left == current:
      return False
    
    if half & 1:
      return True

    half //=2
    if left < current:
      current -= half
    else:
      current += half
 

for i in range(10000000):

    a = random.randint(0, 2**30-1)
    b = random.randint(0, 2**30-1)

    # a = random.randint(0, 10000)
    # b = random.randint(0, 10000)

    if arePairs(a,b) != arePairs2(a, b):
      print(a, b, 'Failed!')
      raise 'Failed'

    if i % 10000 == 0:
      print(i, ':', a, b)



