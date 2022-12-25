from main import init_blossom_params, find_maximum_matching

def test(graph: "dict[int, set[int]]", n: int, expected: int):
    init_blossom_params(graph, n)
    ret = find_maximum_matching(True)
    print(expected == ret, graph, n, ret)

def edges_to_graph(edges):
    graph = {}
    for a, b in edges:
        graph[a] = set()
        graph[b] = set()

    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    return graph


# test({
#     0: set([1]),
#     1: set([0, 2]),
#     2: set([1, 3]),
#     3: set([2])
# }, 4, 4)

# test({
#     2: set([0]),
#     0: set([2, 1]),
#     1: set([0, 3]),
#     3: set([1])
# }, 4, 4)


# test({
#     0: set([1, 2, 3, 4]),
#     1: set([0]),
#     2: set([0]),
#     3: set([0]),
#     4: set([0]),
# }, 5, 2)

# test({
#     0: set([1, 5, 3, 4]),
#     1: set([0, 2]),
#     2: set([1]),
#     3: set([0]),
#     4: set([0]),
#     5: set([0])
# }, 6, 4)

# test({
#     0: set([1,3,5]),
#     1: set([0,4]),
#     2: set([3,4,6]),
#     3: set([0,2]),
#     4: set([1,2]),
#     5: set([0]),
#     6: set([2,7]),
#     7: set([6])
# }, 8, 8)

# test({
#     0: set([1, 8]),
#     1: set([0,2]),
#     2: set([1,3,6]),
#     3: set([2,5]),
#     4: set([5,6]),
#     5: set([3,4]),
#     6: set([2,4,7]),
#     7: set([6,9]),
#     8: set([0]),
#     9: set([7]),
# }, 10, 10)

# test({
#     0: set([1,9]),
#     1: set([0,2]),
#     2: set([1,3,6]),
#     3: set([2,5]),
#     4: set([5,6]),
#     5: set([3,4]),
#     6: set([2,4,7]),
#     7: set([6,8]),
#     8: set([7]),
#     9: set([0]),
# }, 10, 10)

# test(edges_to_graph([
#     [0,3],
#     [0,5],
#     [0,4],
#     [3,4],
#     [3,5],
#     [4,1],
#     [1,5],
#     [2,5],
#     [2,1],
# ]), 6, 6)

# test(edges_to_graph([
#     [6,1],
#     [5,0],
#     [7,2],
#     [3,8],
#     [9,4],
#     [9,10],
#     [10,11],
#     [0,1],
#     [1,3],
#     [3,4],
#     [4,2],
#     [2,0]
# ]), 12, 12)

# test(edges_to_graph([
#     [0,3],
#     [1,2],
#     [3,4],
#     [4,5],
#     [2,5],
#     [3,6],
#     [6,7],
#     [7,8],
#     [4,8],
#     [8,9],
#     [5,9],
#     [2,9]
# ]), 10, 10)


# test(edges_to_graph([
#     [0,1],
#     [0,2],
#     [1,2],
#     [1,3],
#     [3,4],
#     [3,5],
#     [4,5],
#     [4,6],
#     [6,7],
#     [6,8],
#     [7,8],
# ]), 9, 8)

test(edges_to_graph([
    [0,1],
    [0,2],
    [1,2],
    [1,3],
    [3,4],
    [3,5],
    [4,5],
    [4,6],
    [6,7],
    [6,8],
    [7,8],
    [7,9],
    [9,10],
    [9,11],
    [10,11],
]), 12, 12)