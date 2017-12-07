import re


def read_input():
    with open('input.txt') as f:
        return f.read()


def parse_node(line):
    node_id = re.search('^[\w]+', line).group(0)
    weight = int(re.search('\d+', line).group(0))
    links_m = re.search('\w+,.*', line)
    links = links_m.group(0).replace(' ', '').split(',') if links_m else []
    return dict(_id=node_id,
                weight=weight,
                links=links)


def main():
    _input = read_input()
    nodes = [parse_node(line)
             for line in _input.split('\n')
             if line]
    adjacency_list = {node['_id']: node['links']
                      for node in nodes}
    # pt1
    all_links = reduce(lambda acc, links: acc.union(links),
                       adjacency_list.values(),
                       set())
    root_id = set(adjacency_list.keys()).difference(all_links).pop()
    print root_id

    #  pt2
    # node-weight
    self_weight = {node['_id']: node['weight']
                   for node in nodes}

    # node + sub-nodes weight (memoized)
    tree_weight_cache = {}

    def get_tree_weight(_id):
        if _id not in tree_weight_cache:
            tree_weight_cache[_id] = self_weight[_id] + sum(get_tree_weight(link_id)
                                                            for link_id in adjacency_list[_id])
        return tree_weight_cache[_id]
    get_tree_weight(root_id)

    for node_id, links in adjacency_list.items():
        tree_weights = [tree_weight_cache[_id] for _id in links]
        if tree_weights and max(tree_weights) - min(tree_weights):
            print node_id, links
            print self_weight[node_id], tree_weights

if __name__ == '__main__':
    main()
