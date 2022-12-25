from main import arePairs

def testPairs(a,b, expected):
  print(arePairs(a,b) == expected, a, b, arePairs(a,b), )

testPairs(1,1, False)
testPairs(1,2, True)
testPairs(1,3, False)
testPairs(2,3, True)
testPairs(1,4, True)
testPairs(1,5, True)
testPairs(1,6, True)
testPairs(1,7, False)
testPairs(1,8, True)
testPairs(1,9, True)
testPairs(1,10, True)
testPairs(pow(2, 30)-1,2, True)
testPairs(107371823,473262, True)