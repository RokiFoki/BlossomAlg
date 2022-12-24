debug = True
def printDebug(*args):
  if debug: print(*args)

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

graph = {}
n = None
m = None
mate = {}

blossum_verticles = None
verticle_blossum = None
blossum_index = None
def init_blossum_params(_graph, _n): 
  global blossum_verticles, blossum_verticles, blossum_index, verticle_blossum, n, m, mate, graph
  n = _n
  graph = _graph

  m = int(3 * n / 2) # https://codeforces.com/blog/entry/92339
  blossum_verticles = [False] * m
  verticle_blossum = [-1 for _ in range(m)]
  blossum_index = n
  mate = {}

def build_graph(l):
  graph = {}
  n = len(l)

  for i in range(n-1):
    for j in range(i+1, n):
      if arePairs(l[i], l[j]):
        iSet = graph.get(i, set())
        iSet.add(j)
        graph[i] = iSet

        jSet = graph.get(j, set())
        jSet.add(i)
        graph[j] = jSet
  
  return graph, n

def get_depth(v): 
  c = 0
  while p[v] != -1:
    v = p[v]
    c += 1
  
  return c

def reversed(list):
  list.reverse()

  return list

def get_trace(v):
  trace = [v]
  r = v
  while p[r] != -1:
    r = p[r]
    trace.append(r)

  return reversed(trace)



def contract(trace_1, trace_2):
  global blossum_index
  i = 0
  while trace_1[i] == trace_2[i]: i += 1
  i -= 1
  
  v = trace_1[i]

  blossum_path_1 = trace_1[i:]
  blossum_path_2 = trace_2[i:]
  blossum_verticles[blossum_index] = blossum_path_1 + blossum_path_2
  reversed(blossum_path_2)[:-1] # test this
  p[blossum_index] = p[v]

  graph[blossum_index] = set()
  for ver in blossum_verticles[blossum_index]:
    verticle_blossum[ver] = blossum_index

    graph[blossum_index].update(graph[ver])

  if v in mate:
    printDebug('updating match:', blossum_index, '->', mate[v])
    mate[blossum_index] = mate[v]
    mate[mate[v]] = blossum_index
 
  blossum_index += 1


def lift(path):
  printDebug('lifting: path', path)
  lifted_path = []

  i = 0
  while len(path) - i >= 2:
    z = path[i]
    printDebug('lifting: checking', z)
    if z < n: 
      lifted_path.append(z)
      printDebug('lifting: (not glossom) lifted_path', lifted_path)
      i += 1
      continue

    b_index = z
    w = path[i+1]
    printDebug('lifting: (glossom):', blossum_verticles[b_index])

    start = None
    end = None
    diff = None
    k = len(blossum_verticles[b_index])
    if len(lifted_path) % 2 == 0:
      for ver in blossum_verticles[b_index]:
        if w in graph[ver]: # do I need check matching as well?
          start = blossum_verticles[b_index].index(ver)
      
      end = 0

      diff = 1 if start % 2 == 1 else k - 1
    else:
      start = 0

      for ver in blossum_verticles[b_index]:
        if lifted_path[-1] in graph[ver]: # do I need check matching as well?
          end = blossum_verticles[b_index].index(ver)

      diff = 1 if end % 2 == 1 else k - 1

    printDebug('lifting: z:', z, 'start:', start, 'end:', end, 'diff:', diff)
 
    k = len(blossum_verticles[b_index])
    while start != end:
      printDebug('lifting: adding', blossum_verticles[b_index][start])
      path.append(blossum_verticles[b_index][start])
      start = (start + diff) % k
      
    path.append(blossum_verticles[b_index][start])

    printDebug('lifting: (glossom) lifted_path', lifted_path, 'path:', path)

    if b_index in mate: # do we need it
      mate[mate[b_index]] = blossum_verticles[b_index][0] # do we need it
    # do we need to reduce the blossum_index?
   
    i += 1
  
  return lifted_path

p = None
def find_augmenting_path(): 
  global p
  forest = set()
  forest_nodes = set()
  q = []
  verticles_marked = [0 for i in range(m)]
  edges_marked = [[0 for j in range(m)] for i in range(m)]
  p = [-1 for i in range(m)]

  verticles_and_blossoms_n = blossum_index
  for v in range(verticles_and_blossoms_n):
    if v in mate:
      edges_marked[v][mate[v]] = 1 
      edges_marked[mate[v]][v] = 1 

  for v in range(verticles_and_blossoms_n):
    if v not in mate:
      forest.add(v)
      forest_nodes.add(v)
      q.append(v)
  
  i = 0
  printDebug('\nextended verticles:', q)
  while i < len(q): 
    v = q[i]; i += 1
    printDebug('v:', v, '(extended verticle)')

    depth = get_depth(v) # probably not needed as q will always have only even odd depth verticles
    if depth % 2 == 1 or verticles_marked[v]: 
      printDebug('skipping:', v, ':', depth % 2 == 1, verticles_marked[v])
      continue

    neighbours = graph[v]
    if debug: 
      neighbours = list(graph[v])
      neighbours.sort()

    for w in neighbours:
      printDebug("w:", w, "(v's neighbour)")
      while verticle_blossum[w] != -1: w = verticle_blossum[w]
      printDebug("(w) finding its blossum if it is in one:", w)

      if edges_marked[v][w]: 
        printDebug("(w) edge was already processed")
        continue
      
      if w not in forest_nodes:
        printDebug("(w) it is not in a forest")
        x = mate[w]

        p[w] = v
        p[x] = w
        forest_nodes.add(w)
        forest_nodes.add(x)

        printDebug('updatedTreePath:', get_trace(x) if debug else None)

        q.append(x) # only even ones need to be processed
      else:
        printDebug("(w) it is in the forest")
        if get_depth(w) % 2 == 1:
          i += 1
          printDebug("(w) its depth is odd. Skipping")
          continue
        else:
          printDebug("(w) its depth is even")
          trace_v = get_trace(v)
          printDebug("(trace v)", trace_v)
          trace_w = get_trace(w)
          printDebug("(trace w)", trace_w)
          if trace_v[0] != trace_w[0]:
            printDebug("(v, w) don't have same root")
            path = trace_v + reversed(trace_w)

            printDebug('augmented path found:', path)
            return path
          else:
            printDebug('(v,w) have same root, contracting')
            contract(trace_v, trace_w)
            # todo: new graph, new mates
            path = find_augmenting_path()
            printDebug('(v,w) path after contraction:', path)
            
            return lift(path)
      
      edges_marked[v][w] = edges_marked[w][v] = 1
    
    verticles_marked[v] = 1

  return []

def augment(path):
  i = 0

  printDebug('calculating new matching from path', path)
  while i + 1 < len(path):
    mate[path[i]] = path[i+1]
    mate[path[i+1]] = path[i]
    printDebug('new matching pair:', path[i], '->', path[i+1])

    i += 2

def mathching_to_string():
  if not debug: return None
  keys = []

  for key in mate:
    if int(key) < mate[key]: keys.append(str(key) + '->' + str(mate[key]))
  return ', '.join(keys)
  

res = 0
def find_maximum_matching(_debug=False):
  global res, debug

  debug = _debug
  path = find_augmenting_path()
  if path:
    augment(path)
    printDebug('new matching:', mathching_to_string())
    res += 2
    return find_maximum_matching(_debug)
  
  printDebug('no path found:', path, 'matching:', mathching_to_string())
  return res

def get_matched_verticles(): 
  return res

def solution(l):
  graph, n = build_graph(l)
  init_blossum_params(n, graph)

  find_maximum_matching()

  return n - get_matched_verticles()




