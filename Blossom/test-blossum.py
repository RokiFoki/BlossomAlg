from main import init_blossum_params, find_maximum_matching

def test(graph: "dict[int, set[int]]", n: int):
    init_blossum_params(graph, n)
    ret = find_maximum_matching(True)
    print(graph, n, ret)


test({
    0: set([1]),
    1: set([0, 2]),
    2: set([1, 3]),
    3: set([2])
}, 4)