def read_input():
    with open('input.txt') as f:
        return f.readlines()


def parse_line(line):
    """Parse a line of the input.

    eg. id <-> link_id[,link_id..]

    Returns
    -------
    (int, set[int])
    node-id, linked node-ids
    """
    tokens = line.split()
    return (int(tokens[0]),
            {int(_id.replace(',', ''))
                for _id in tokens[2:]})


def bfs(node_id, adjacency_list, process_node_func):
    """breadth-first-search.

    Parameters
    ----------
    node_id: int
    adjacency_list: dict[int, list[int]]
    process_node_func: int -> None
    """
    processed = set()
    queue = [node_id]
    while len(queue):
        cur_node = queue.pop(0)
        processed.add(cur_node)
        linked_nodes = adjacency_list[cur_node]
        for linked_node in linked_nodes:
            if linked_node not in processed and linked_node not in queue:
                queue.append(linked_node)
        process_node_func(cur_node)


def main():
    _input = read_input()
    adjacency_list = dict(parse_line(line)
                          for line in _input
                          if line)
    nodes = set()

    def add_node(node_id):
        nodes.add(node_id)

    # part 1
    bfs(0, adjacency_list, add_node)
    print '# nodes connected to node 0', len(nodes)

    # part 2
    nodes.clear()

    remaining_nodes = set(adjacency_list.keys())
    connected_components = 0
    while len(remaining_nodes):
        node_id = remaining_nodes.pop()
        bfs(node_id, adjacency_list, add_node)
        remaining_nodes = remaining_nodes.difference(nodes)
        connected_components += 1
    print '# connected components ', connected_components


if __name__ == '__main__':
    main()
