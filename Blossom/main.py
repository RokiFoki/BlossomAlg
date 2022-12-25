debug = False
def printDebug(*args):
  if debug: print(args)
  #if debug: print(*args)

def arePairs(a, b): 
  seen = set()
  
  low = min(a, b)
  high = max(a, b)
  while low != high:
    if (low+high) % 2 == 1: return True
    if (low+high) % 4 == 2: return low != high

    a2 = high - low
    b2 = low * 2

    low = min(a2, b2)
    high = max(a2, b2)

    
    if low in seen: return True
    if high in seen: return True

    if low % 2 == 0 and high % 2 == 0:
      low = low / 2
      high = high / 2
      seen = set()

    seen.add(low)
    seen.add(high)
 

  return False

graph = {}
n = None
m = None
mate = {}

blossom_verticles = None
verticle_blossom = None
blossom_index = None
res = 0
def init_blossom_params(_graph, _n): 
  global blossom_verticles, blossom_verticles, blossom_index, verticle_blossom, n, m, mate, graph, res
  n = _n
  graph = _graph

  m = int(3 * n / 2) # https://codeforces.com/blog/entry/92339
  blossom_verticles = [False] * m # keeps verticles/inner blossoms that are contained in i-th blossom
  verticle_blossom = [-1 for _ in range(m)] # keeps blossom index (i) of verticle at i-th position
  blossom_index = n # next blossom index
  mate = {} # matching is kept/updated in this dict
  res = 0

def build_graph(l):
  graph = {}
  n = len(l)

  for i in range(n):
    graph[i] = set();

  for i in range(n-1):
    for j in range(i+1, n):
      if arePairs(l[i], l[j]):
        graph[i].add(j)
        graph[j].add(i)
        
  return graph, n

def get_depth(v): 
  c = 0
  while parent[v] != -1:
    v = parent[v]
    c += 1
  
  return c

def reversed(list):
  list.reverse()

  return list

def get_trace(v):
  trace = [v]
  r = v
  while parent[r] != -1:
    r = parent[r]
    trace.append(r)

  return reversed(trace)



def contract(trace_1, trace_2):
  global blossom_index
  i = 0
  while i < min(len(trace_1), len(trace_2)) and trace_1[i] == trace_2[i]: i += 1
  i -= 1
  
  v = trace_1[i]

  blossom_path_1 = trace_1[i:]
  blossom_path_2 = trace_2[i:]
  blossom_verticles[blossom_index] = blossom_path_1 + reversed(blossom_path_2)[:-1]
  parent[blossom_index] = parent[v]

  # insert blossom in graph
  graph[blossom_index] = set()
  for ver in blossom_verticles[blossom_index]:
    verticle_blossom[ver] = blossom_index

    graph[blossom_index].update(graph[ver])

  for ver in graph[blossom_index]:
    graph[ver].add(blossom_index)

  if v in mate:
    printDebug('updating match:', blossom_index, '->', mate[v])
    mate[blossom_index] = mate[v]
    mate[mate[v]] = blossom_index
 
  blossom_index += 1

  return blossom_index - 1


def lift(path, b_index):
  printDebug('lifting: path', path)
  lifted_path = []

  i = 0
  while i < len(path):
    v = path[i]
    printDebug('lifting: checking', v)
    if b_index != v: 
      lifted_path.append(v)
      printDebug('lifting: lifted_path', lifted_path)
      i += 1
      continue

    printDebug('lifting: (glossom):', blossom_verticles[b_index])

    start = None
    end = None
    diff = None
    k = len(blossom_verticles[b_index])
    if i % 2 == 0:
      start = 0 # something, from outside is matched to it, or it's the first verticle (and it needs to be exposed (the only non inner matched verticle in the blossom))
      
      if i + 1 < len(path):
        next_v = path[i+1]
        printDebug('lifting: next_v', next_v)
        for indx, blossom_verticle in enumerate(blossom_verticles[b_index]):
          if next_v in graph[blossom_verticle] and indx != 0: # must be a inner matched edge. 0 edge is the only one that is not inner matched (can be matched only with outside)
            end = indx
            break
        else: 
          end = 0 # this is possible only if there is no verticles before blossom
          if len(lifted_path) > 0: printDebug('lifting: this should never happen (end) !!!!!!!')
      else:
        end = 0 # if there is no next verticle, after blossom, we need to end in exposed verticle
    else: 
      # i is odd (blossom is matched to the next verticle, or there is no next verticle - either way, end is 0 (the only non inner matched verticle in the blossom))
      end = 0

      # there is a node before (i is odd and positive)
      prev_v = lifted_path[-1]
      printDebug('lifting: prev_v', prev_v)
      for indx, blossom_verticle in enumerate(blossom_verticles[b_index]):
        if prev_v in graph[blossom_verticle] and indx != 0: # must be a inner matched edge. 0 edge is the only one that is not inner matched (can be matched only with outside) - one exception (check the for else comment)
          start = indx
          break
      else:
        start = 0 # it is possible to be non inner matched edge, but then there should be no next verticle, and we need to end in an exposed verticle
        if i+1 < len(path): printDebug('lifting: this should never happen (start) !!!!!!!')

    if start == end: 
      diff = 1 # can be anything as we will not enter the whle loop
    else:
      # detect the direction, we need to pass the "matched" edge as the outside edge must be non matched in the aug path 
      path_important_node = blossom_verticles[b_index][end] if start == 0 else blossom_verticles[b_index][start]
      from_node_to_important_node = mate[path_important_node]

      printDebug('lifting: from_node_to_important_node', from_node_to_important_node, 'important_node', path_important_node)

      _diff = blossom_verticles[b_index].index(path_important_node) - blossom_verticles[b_index].index(from_node_to_important_node)
      diff = (1 if start == 0 else -1) * _diff  + k
    
    printDebug('lifting: b_index:', b_index, 'start:', start, 'end:', end, 'diff:', diff)
    
    while start != end:
      printDebug('lifting: adding', blossom_verticles[b_index][start])
      lifted_path.append(blossom_verticles[b_index][start])
      start = (start + diff) % k
    
    printDebug('lifting: adding', blossom_verticles[b_index][start])  
    lifted_path.append(blossom_verticles[b_index][start])

    printDebug('lifting: (glossom) lifted_path', lifted_path, 'path:', path)

    i += 1

  # remove blossom from graph
  for ver in blossom_verticles[b_index]:
    verticle_blossom[ver] = -1

  for ver in graph[b_index]:
    graph[ver].remove(b_index)

  del graph[b_index]

  if b_index in mate:
    mate[mate[b_index]] = blossom_verticles[b_index][0] # 0 index verticle is the only non inner matched verticle
    del mate[b_index]
  
  return lifted_path

parent = None
def find_augmenting_path(): 
  global parent
  forest_nodes = set()
  queue = []
  verticles_marked = [0 for _ in range(m)]
  edges_marked = [[0 for _ in range(m)] for _ in range(m)]
  parent = [-1 for _ in range(m)]

  verticles_and_blossoms_n = blossom_index
  printDebug('verticle_blossom:', verticle_blossom)
  for v in range(verticles_and_blossoms_n):
    if v in mate:
      edges_marked[v][mate[v]] = 1 
      edges_marked[mate[v]][v] = 1 

  for v in range(verticles_and_blossoms_n):
    if verticle_blossom[v] != -1: continue
    if v not in mate:
      forest_nodes.add(v)
      queue.append(v)
  
  i = 0
  printDebug('\nextended verticles:', queue)
  
  while i < len(queue): 
    v = queue[i]; i += 1
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
      if verticle_blossom[w] != -1: continue

      printDebug("w:", w, "(v's neighbour)")

      if edges_marked[v][w]: 
        printDebug("(w) edge was already processed")
        continue
      
      if w not in forest_nodes:
        printDebug("(w) it is not in a forest")
        x = mate[w]

        parent[w] = v
        parent[x] = w
        forest_nodes.add(w)
        forest_nodes.add(x)

        printDebug('updatedTreePath:', get_trace(x) if debug else None)

        queue.append(x) # only even ones need to be processed
      else:
        printDebug("(w) it is in the forest")
        if get_depth(w) % 2 == 1:
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
            blosum_id = contract(trace_v, trace_w)
            
            path = find_augmenting_path()
            printDebug('(v,w) path after contraction:', path)
            
            return lift(path, blosum_id)
      
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
  

def find_maximum_matching(_debug=False):
  global res, debug, blossom_index

  debug = _debug
  path = find_augmenting_path()
  if path:
    augment(path)
    printDebug('new matching:', mathching_to_string())
    res += 2

    blossom_index = n
    return find_maximum_matching(_debug)
  
  printDebug('no path found:', path, 'matching:', mathching_to_string())
  return res

def get_matched_verticles(): 
  return res

def solution(l, _debug=False):
  graph, n = build_graph(l)
  init_blossom_params(graph, n)

  find_maximum_matching(_debug)

  return n - get_matched_verticles()
