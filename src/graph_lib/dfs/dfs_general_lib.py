__all__ = ['dfs', 'dfs_order']

def dfs(graph, start, visited=None):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if visited == None:
        visited = set()
    visited.add(start)
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

def dfs_order(graph, start):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    visited = {start}
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    return order