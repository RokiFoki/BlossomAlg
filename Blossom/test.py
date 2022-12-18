def arePairs(a, b): 
  if (a+b) % 2 == 1: return True

  seen = set()
  
  low = min(a, b)
  high = max(a, b)
  while low != high:
    a2 = high - low
    b2 = low * 2

    low = min(a2, b2)
    high = max(a2, b2)

    if low in seen: return True
    if high in seen: return True

    seen.add(low)
    seen.add(high)

  return False


def solution(l):
  n = len(l)

  pairs = {}
  for i in range(n-1):
    for j in range(i+1, n):
      areP = arePairs(l[i], l[j])

      pairs.get(i, set()).add(j)
      pairs.get(j, set()).add(i)

  connections = [len(pairs[i]) for i in range(n)]
  def solve(i):  
    

  return solve()


def testPairs(a,b):
  print(a, b, arePairs(a,b))


def test(n):
  print(n, solution(n))


testPairs(1,1)
testPairs(1,2)
testPairs(1,3)
testPairs(1,4)
testPairs(1,5)
testPairs(1,6)
testPairs(1,7)
testPairs(1,8)
testPairs(1,9)
testPairs(1,10)

