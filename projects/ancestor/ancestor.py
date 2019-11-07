
def earliest_ancestor(ancestors, starting_node):
    parents = dict()
    for children in ancestors:
      child = children[1]
      if child not in parents:
        parents[child] = set()
      parents[child].add(children[0])
    parent = None
    if starting_node not in parents:
      return -1
    parent = parents[starting_node][1]
    while