
def earliest_ancestor(ancestors, starting_node):
    parents = dict()
    for children in ancestors:
      child = children[1]
      if child not in parents:
        parents[child] = set()
      parents[child].add(children[0])
    