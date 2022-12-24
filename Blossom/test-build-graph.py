from main import build_graph

def test(l):
    graph = build_graph(l)
    print('For', l)
    print(graph)
    print('------')

test([])
test([1])
test([1,2])
test([1,2,3])
test([1,2,3,4])
test([1,2,3,4,5])
test([1,2,3,4,5,6])
test([1,2,3,4,5,6,7,8])