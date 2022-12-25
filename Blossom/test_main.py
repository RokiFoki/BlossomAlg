
from main import solution

def test(list, exepcted):
    ret = solution(list, True)
    print(ret == exepcted, list, ret)


#test([1,1], 2)
#test([1, 7, 3, 21, 13, 19], 0)
test([1,2,3,4,5,6], 0)