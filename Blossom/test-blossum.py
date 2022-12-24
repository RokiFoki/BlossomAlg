from main import init_blossum_params, find_maximum_matching

def test(graph: "dict[int, set[int]]", n: int):
    init_blossum_params(graph, n)
    ret = find_maximum_matching(True)
    print(graph, n, ret)


# test({
#     0: set([1]),
#     1: set([0, 2]),
#     2: set([1, 3]),
#     3: set([2])
# }, 4)

# test({
#     2: set([0]),
#     0: set([2, 1]),
#     1: set([0, 3]),
#     3: set([1])
# }, 4)


# test({
#     0: set([1, 2, 3, 4]),
#     1: set([0]),
#     2: set([0]),
#     3: set([0]),
#     4: set([0]),
# }, 5)

# test({
#     0: set([1, 5, 3, 4]),
#     1: set([0, 2]),
#     2: set([1]),
#     3: set([0]),
#     4: set([0]),
#     5: set([0])
# }, 6)

# test({
#     0: set([1,3,5]),
#     1: set([0,4]),
#     2: set([3,4,6]),
#     3: set([0,2]),
#     4: set([1,2]),
#     5: set([0]),
#     6: set([2,7]),
#     7: set([6])
# }, 8)

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
# }, 10)

test({
    0: set([1,9]),
    1: set([0,2]),
    2: set([1,3,6]),
    3: set([2,5]),
    4: set([5,6]),
    5: set([3,4]),
    6: set([2,4,7]),
    7: set([6,8]),
    8: set([7]),
    9: set([0]),
}, 10)